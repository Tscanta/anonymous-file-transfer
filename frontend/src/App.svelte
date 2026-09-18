<script lang="ts">
  let dropCode = "";
</script>

<main>
  <div class="container">
    <h1>Anonymous Transfer</h1>

    <p class="subtitle">
      Move files between devices without signing in.
    </p>

    <button class="create-button">
      Create a Drop
    </button>

    <div class="divider">
      <span>or</span>
    </div>

    <div class="open-drop">
      <label for="dropCode">Drop Code</label>

      <input
        id="dropCode"
        type="text"
        placeholder="Enter your drop code"
        bind:value={dropCode}
      />

      <button class="open-button">
        Open Drop
      </button>
    </div>
  </div>
</main>

<style>
  :global(*) {
    box-sizing: border-box;
  }

  :global(body) {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f5f5;
  }

  main {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .container {
    width: 100%;
    max-width: 450px;
    padding: 40px;
    background: white;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  }

  h1 {
    margin: 0;
    font-size: 32px;
  }

  .subtitle {
    color: #666;
    margin: 12px 0 30px;
  }

  button {
    width: 100%;
    padding: 14px;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
  }

  .create-button {
    background: #111;
    color: white;
  }

  .divider {
    margin: 25px 0;
    color: #999;
  }

  .open-drop {
    text-align: left;
  }

  label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
  }

  input {
    width: 100%;
    padding: 14px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
    margin-bottom: 12px;
  }

  .open-button {
    background: #eee;
    color: #111;
  }
</style>