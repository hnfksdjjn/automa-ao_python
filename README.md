 **O código envia mensagens automáticas no WhatsApp para várias pessoas.**

**1. Importa bibliotecas:**
- `time`: pausa a execução.
- `pyautogui`: controla mouse e teclado.

**2. Abre o WhatsApp:**
- Simula pressionar a tecla "Windows", digitar "WhatsApp" e pressionar "Enter".

**3. Loop para enviar mensagens:**
- Percorre uma lista de nomes e mensagens.
- Para cada pessoa:
    - Digita o nome na barra de busca.
    - Clica no botão "Abrir" da conversa.
    - Digita a mensagem.
    - Pressiona "Enter" para enviar.
    - Clica em algum lugar da tela (possivelmente para fechar a conversa).

**4. Finaliza:**
- Exibe um alerta "Saindo do loop".
 **O código envia mensagens automáticas no WhatsApp para várias pessoas.**

**1. Importa bibliotecas:**
- `time`: pausa a execução.
- `pyautogui`: controla mouse e teclado.

**2. Abre o WhatsApp:**
- Simula pressionar a tecla "Windows", digitar "WhatsApp" e pressionar "Enter".

**3. Loop para enviar mensagens:**
- Percorre uma lista de nomes e mensagens.
- Para cada pessoa:
    - Digita o nome na barra de busca.
    - Clica no botão "Abrir" da conversa.
    - Digita a mensagem.
    - Pressiona "Enter" para enviar.
    - Clica em algum lugar da tela (possivelmente para fechar a conversa).

**4. Finaliza:**
- Exibe um alerta "Saindo do loop".

 **O código automatiza a pesquisa no Google Chrome, simulando ações como se você digitasse e clicasse.**

**1. Importa ferramentas:**
- `pyautogui`: controla mouse e teclado.
- `time`: pausa a execução.

**2. Pede o que pesquisar:**
- `pesquisa = input("digite o que voce quer pesquisa: ")`

**3. Abre o Chrome:**
- `pyautogui.press("win")`: abre menu iniciar.
- `pyautogui.write("chrome")`: escreve "chrome".
- `pyautogui.press("enter")`: abre Chrome.

**4. Acessa o Google:**
- `pyautogui.write("google")`: escreve "google" na barra de endereço.
- `pyautogui.press("enter")`: acessa página da busca.

**5. Digita a pesquisa:**
- `pyautogui.write(f"{pesquisa}")`: escreve o que você digitou.

**6. Realiza a busca:**
- `pyautogui.press("enter")`: inicia a busca.
