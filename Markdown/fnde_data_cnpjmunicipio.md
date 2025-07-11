# Dicionário de Dados Modelo

A tabela fnde_data_cnpjmunicipio armazena a correspondência entre os CNPJs das entidades executoras municipais (como prefeituras, fundos ou secretarias de educação) e o código interno do sistema SISCACS, que funciona como uma chave de negócio dentro do ecossistema FNDE.

Ela atua como tabela de referência e é essencial para:

Garantir a unicidade dos CNPJs utilizados nos sistemas FNDE;

Viabilizar junções com tabelas financeiras e administrativas;

Fazer a tradução entre CNPJs e os códigos SISCACS, que podem ser utilizados em outras tabelas como chave estrangeira

## Tabela `fnde_data_cnpjmunicipio`

| Campo          | Tipo                   | Chave       | Descrição                                                                                                                             | Relacionamento Possível                                                                                                     |
| -------------- | ---------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `id`           | bigint (autoincrement) | Primary Key | Identificador único da linha. Utilizado para **indexação e relacionamentos técnicos**.                                                | Pode ser referenciado por outras tabelas que queiram manter vínculo técnico (FK para `fnde_data_cnpjmunicipio.id`).         |
| `cnpj`         | varchar(20)            | Unique      | Cadastro Nacional da Pessoa Jurídica da entidade municipal (pode ter sufixo adicional usado internamente).                            | Pode ser usado para cruzamento com tabelas de pagamento, saldo ou execução (ex: `pagamentos.cnpj`, `saldo.cnpj`).           |
| `siscacs_code` | varchar(10)            | Indexável   | Código da unidade no sistema **SISCACS/FNDE**, utilizado como chave de negócio para **vincular os dados institucionais** da entidade. | Altamente provável ser chave estrangeira para tabelas operacionais que contenham `siscacs_code` como referência à entidade. |

 🔗 Relacionamentos Identificados:
 
| Campo          | Relaciona-se com…                                                                        | Tipo de Relacionamento       |
| -------------- | ---------------------------------------------------------------------------------------- | ---------------------------- |
| `id`           | Pode ser chave primária referenciada em tabelas auxiliares internas do modelo            | FK técnica (surrogate key)   |
| `cnpj`         | Tabelas de pagamentos, saldos, execução                                                  | Cruzamento de dados externos |
| `siscacs_code` | Tabelas operacionais e financeiras do FNDE (ex: `execucao_programa`, `prestacao_contas`) | Chave de negócio             |
                                    |


### Índices
- Index em (`id`, `cnpj`, `siscacs_code`) conforme definido em `Meta.indexes`.