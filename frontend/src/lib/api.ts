const API_URL = "http://127.0.0.1:8000";

export async function createDrop() {
  const response = await fetch(`${API_URL}/drops`, {
    method: "POST"
  });

  if (!response.ok) {
    throw new Error("Failed to create drop");
  }

  return await response.json();
}