const opcoesCadastro = document.querySelectorAll('input[name="tipo-cadastro"]');
const dadosEstabelecimento = document.querySelector('#dados-estabelecimento');

opcoesCadastro.forEach(function(opcao) {
  opcao.addEventListener('change', function() {

    if (opcao.value === 'representante') {
      dadosEstabelecimento.hidden = false;
    } else {
      dadosEstabelecimento.hidden = true;
    }

  });
});