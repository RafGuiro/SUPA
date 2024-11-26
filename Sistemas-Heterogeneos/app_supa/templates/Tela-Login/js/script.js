function validateForm() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (email === "" || password === "") {
        alert("Por favor, preencha todos os campos.");
        return false;  // Impede o envio do formulário se não estiver preenchido
    }
    
    // Redireciona para a página de cadastro (sem impedir o envio)
    window.location.href = "../Tela-Cad_paciente/index.html";
    return true;  // Permite o envio do formulário após o redirecionamento
}
