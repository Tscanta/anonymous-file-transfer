<script lang="ts">
  import { createDrop } from "./lib/api";

  let dropCode = "";
  let createdDropCode = "";
  let loading = false;
  let error = "";

  async function handleCreateDrop() {
    loading = true;
    error = "";

    try {
      const data = await createDrop();

      createdDropCode = data.drop_id;
    } catch (err) {
      error = "Could not create drop.";
    } finally {
      loading = false;
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

            <button
              class="retro-button"
              onclick={handleCreateDrop}
              disabled={loading}
            >
              {loading ? "Creating..." : "📄  Create a Drop"}
            </button>

            <small>
              Generate a unique code to start sharing.
            </small>

            {#if createdDropCode}
              <div class="drop-created">
                <div class="drop-created-title">
                  DROP CREATED!
                </div>

                <div class="drop-code">
                  {createdDropCode}
                </div>

                <p>
                  Enter this code on another device to access your files.
                </p>
              </div>
            {/if}

            {#if error}
              <div class="error">
                {error}
              </div>
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

            <button class="retro-button">
              📁 &nbsp; Open Drop
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