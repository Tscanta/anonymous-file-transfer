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


export async function uploadFile(dropId: string, file: File) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    `${API_URL}/drops/${dropId}/files`,
    {
      method: "POST",
      body: formData
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to upload ${file.name}`);
  }

  return await response.json();
}