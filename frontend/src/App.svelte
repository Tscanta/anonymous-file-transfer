<script lang="ts">
  import { createDrop, uploadFile, getDrop } from "./lib/api";

  let selectedFiles: File[] = [];
  let dropCode = "";

  let creating = false;
  let error = "";

  let openedDrop: {
  drop_id: string;
  files: {
    file_id: string;
    filename: string;
  }[];
} | null = null;

let opening = false;
let openError = "";

  function handleFiles(event: Event) {
    const input = event.target as HTMLInputElement;

    if (input.files) {
      selectedFiles = Array.from(input.files);
    }
  }

  async function handleCreateDrop() {
    if (selectedFiles.length === 0) {
      return;
    }

    creating = true;
    error = "";

    try {
      // 1. Create the Drop
      const drop = await createDrop();

      dropCode = drop.drop_id;

      // 2. Upload every selected file
      for (const file of selectedFiles) {
        await uploadFile(dropCode, file);
      }

    } catch (err) {
      console.error(err);
      error = "Could not create drop or upload files.";
    } finally {
      creating = false;
    }
  }
  async function handleOpenDrop() {
  if (!dropCode.trim()) {
    openError = "Please enter a drop code.";
    return;
  }

  opening = true;
  openError = "";
  openedDrop = null;

  try {
    const data = await getDrop(
      dropCode.trim().toUpperCase()
    );

    openedDrop = data;

  } catch (err) {
    console.error(err);

    if (err instanceof Error) {
      openError = err.message;
    } else {
      openError = "Could not open drop.";
    }

  } finally {
    opening = false;
  }
}
</script>

<svelte:head>
  <title>zebraAFT - Anonymous File Transfer</title>
</svelte:head>

<div class="page">

  <header class="header">
    <div class="logo">
      <span class="logo-main">zebra<span>AFT</span></span>
      <span class="logo-sub">anonymous file transfer</span>
    </div>

    <div class="tagline">
      same files.<br />
      different places.<br />
      no accounts.
    </div>
  </header>


  <div class="layout">

    <aside class="sidebar">

      <section class="panel">
        <div class="panel-title">:: navigation</div>

        <div class="nav">
          <a href="/">&gt; home</a>
          <a href="/">&gt; about</a>
          <a href="/">&gt; faq</a>
          <a href="/">&gt; source</a>
        </div>
      </section>


      <section class="panel">
        <div class="panel-title">:: status</div>

        <div class="status">
          <div>
            <span class="status-light"></span>
            server online
          </div>

          <div>
            <span class="status-light"></span>
            no login required
          </div>

          <div>
            <span class="status-light"></span>
            anonymous mode
          </div>
        </div>
      </section>

    </aside>


    <main class="content">

      <section class="panel welcome">

        <div class="panel-title">
          :: welcome to zebraAFT
        </div>

        <div class="welcome-body">

          <h1>Share files between devices.</h1>

          <p>
            No accounts. No tracking. Just files.
          </p>


          <div class="action">
            <label class="file-picker">
              📁 &nbsp; Select Files

              <input
                type="file"
                multiple
                onchange={handleFiles}
              />
            </label>

            <small>
              Select the files you want to transfer.
            </small>


            {#if selectedFiles.length > 0}

              <div class="selected-files">

                <div class="selected-title">
                  {selectedFiles.length} file(s) selected:
                </div>

                {#each selectedFiles as file}
                  <div class="file-item">
                    📄 {file.name}
                  </div>
                {/each}
              </div>
              <button
                class="retro-button"
                onclick={handleCreateDrop}
                disabled={creating}
              >
                {creating ? "Creating Drop..." : "📃  Create Drop"}
              </button>

              {#if dropCode}
                <div class="drop-created">

                  <div class="drop-created-title">
                    DROP CREATED!
                  </div>

                  <div class="drop-code">
                    {dropCode}
                  </div>

                  <p>
                    Your files are ready.
                    Enter this code on another device.
                  </p>

                </div>
              {/if}

              {#if error}
                <div class="error">
                  {error}
                </div>
              {/if}
            {/if}
          </div>


          <div class="or">
            <span>────────</span>
            <b>or</b>
            <span>────────</span>
          </div>


          <div class="action">

            <label for="dropCode">
              Enter a drop code
            </label>

            <input
              id="dropCode"
              type="text"
              placeholder="e.g. K7X2P9QM"
              bind:value={dropCode}
              maxlength="8"
            />

            <button
              class="retro-button"
              onclick={handleOpenDrop}
              disabled={opening}
            >
              {opening ? "Opening Drop..." : "📁  Open Drop"}
            </button>

          </div>

        </div>

      </section>

    </main>


    <aside class="sidebar right">

      <section class="panel">

        <div class="panel-title">
          :: info
        </div>

        <div class="info">

          <p>Fast.</p>
          <p>Simple.</p>
          <p>Anonymous.</p>
          <p>Built for everyone.</p>

          <div class="globe">
            🌐
          </div>

          <p class="quote">
            "A simpler internet<br />
            is possible."
          </p>

          <hr />

          <p>
            v0.1.0<br />
            zebraAFT
          </p>

        </div>

      </section>

    </aside>

  </div>

  {#if openedDrop}
  <section class="drop-view panel">

    <div class="panel-title">
      :: drop {openedDrop.drop_id}
    </div>

    <div class="drop-view-body">

      <h2>Files in this drop</h2>

      {#if openedDrop.files.length === 0}

        <p class="empty-drop">
          This drop is empty.
        </p>

      {:else}

        <div class="file-list">

          {#each openedDrop.files as file}

            <div class="file-row">

              <div class="file-name">
                📄 {file.filename}
              </div>

              <a
                class="download-button"
                href={`http://127.0.0.1:8000/files/${file.file_id}/download`}
              >
                ↓ Download
              </a>

            </div>

          {/each}

        </div>

      {/if}

    </div>

  </section>
{/if}

{#if openError}
  <div class="open-error">
    {openError}
  </div>
{/if}

  <footer>

    <span>
      © 2025 zebraAFT
    </span>

    <span class="footer-links">
      <a href="/">privacy</a>
      |
      <a href="/">terms</a>
      |
      <a href="/">github</a>
    </span>

  </footer>

</div>