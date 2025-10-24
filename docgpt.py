from docx import Document
from openai import OpenAI

def load_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def chat_about_doc(client, text):
    print("Type your question about the document (or 'quit' to exit).")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions about a document."},
                {"role": "user", "content": f"Document:\n{text}\n\nQuestion: {question}"}
            ],
            max_tokens=400
        )
        print("\nDocGPT:", response.choices[0].message.content.strip())

def main():
    client = OpenAI(api_key="")
    path = input("Enter path to your .docx file: ").strip()
    text = load_docx(path)
    print(f"Loaded {len(text.split())} words from {path}")
    chat_about_doc(client, text)

if __name__ == "__main__":
    main()
