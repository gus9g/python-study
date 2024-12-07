SABEMOS QUE A MAIORIA NÃO LERA ESTE ARQUIVO, SE VOCÊ ESTA LENDO, É PORQUE QUER ENTENDER MELHOR SOBRE
O SEU FUNCIONAMENTO...

Esse script tem como foco automatizar o processo de inclusão das libs de projeto Java ao .classpath
por se tratar de uma melhoria de versão do script, foi alterado:
- Limpeza do Código, agora todo o script esta em um único arquivo python
- Geração de planilha resetada, caso tenha apagado a planilha de atualização, não entre em panico,
execute o script, e sera gerada uma nova planilha com os dados de exemplo. Atualize-a e execute novamente
o script
- Preenchimento dos campos: caminho do projeto e quantidade de linhas da planilha,diretamente na planilha
de atualização


Correções Futuras:
- Se executar o script no mesmo projeto, verificar se o arquivo .classpath esta resetado, porque se ja estiver
atualiza-lo o script ira incluir mais uma vez as libs informadas o que ira ocasionar duplicidade de libs.
- Criar um backup automatico do classpath, utilizando um comando de clone do sistema operacional(OS)
