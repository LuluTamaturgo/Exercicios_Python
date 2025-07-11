# Tabela : fnde_data_cnpjmunicipio

Esta tabela mantém a relação de CNPJs de entes municipais (prefeituras, fundos ou secretarias de educação) com o código interno atribuído pelo sistema SISCACS/FNDE.
Serve como camada de referência para:

* validar a unicidade de cada CNPJ no ecossistema FNDE;
* cruzar dados financeiros (pagamentos, saldos) com metadados institucionais;
* agilizar junções entre bases que usam o código SISCACS como chave de negócio.

## Tabela `fnde_data_cnpjmunicipio`

| **Coluna**     | **Tipo de Dado**          | **Descrição**                                                                                                                                                                                                                                               |
| -------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | PrimaryKey - Autoincrement| Identificador único da linha na tabela. Usado como chave primária para indexação e relacionamento com outras tabelas.                                                                                                                                       |
| `cnpj`         | Varchar(20)               | Cadastro Nacional de Pessoa Jurídica. Identifica a entidade vinculada ao município responsável pela execução dos programas do FNDE. Pode conter dígitos extras além dos 14 tradicionais, possivelmente por conter a raiz + sufixo de identificação interna. |
| `siscacs_code` | Varchar(10)               | Código da unidade ou entidade no sistema **SISCACS** (Sistema Integrado de Monitoramento Execução e Controle do FNDE). Esse código é utilizado para localizar ou associar os dados da entidade nos sistemas do FNDE.                                        |


### Índices
- Index em (`id`, `cnpj`, `siscacs_code`) conforme definido em `Meta.indexes`.
