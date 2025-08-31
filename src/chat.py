from search import search_prompt


def main():
    print("=== Sistema de Chat ===")
    print("Digite suas perguntas e pressione Enter.")
    print("Digite 'exit' para sair.\n")

    while True:
        try:
            # Get user input
            question = input("Sua pergunta: ").strip()

            # Check if user wants to exit
            if question.lower() == "exit":
                print("Encerrando o chat. Até logo!")
                break

            # Skip empty questions
            if not question:
                print("Por favor, digite uma pergunta válida.\n")
                continue

            # Get response from search system
            print("Processando...")
            response = search_prompt(question)

            if not response:
                print("Não foi possível processar sua pergunta. Tente novamente.\n")
                continue

            # Print the response
            print(f"\nResposta: {response.content}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\n\nEncerrando o chat. Até logo!")
            break
        except Exception as e:
            print(f"Erro: {str(e)}")
            print("Tente novamente.\n")


if __name__ == "__main__":
    main()
