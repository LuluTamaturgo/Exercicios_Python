🗂️ Tabela fnde_data_fndeprogramas
Esta tabela armazena informações de repasses financeiros feitos pelo FNDE (PNAE, PDDE, PNATE, etc.) para entes federados. Cada linha representa um pagamento (ordem bancária).

🔍 Descrição de Campos

| Campo              | Tipo SQL        | Descrição                                                                                      | Relacionamento Possível                                                     |
| ------------------ | --------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`               | `bigint` (PK)   | Identificador técnico único da linha. Usado para indexação e auditoria.                        | —                                                                           |
| `ano`              | `int`           | Ano de referência do repasse (ex: 2024). Útil para agrupamentos, análises anuais.              | —                                                                           |
| `uf`               | `varchar(2)`    | Sigla da unidade federativa beneficiada (ex: “BA”, “SP”).                                      | → pode se unir a outras tabelas via `uf`                                    |
| `municipio_codigo` | `varchar(10)`   | Código IBGE do município beneficiado.                                                          | 🔗 `fnde_data_convenio.codIbge` <br> 🔗 `portaria_2023_07b.municipality_id` |
| `municipio_nome`   | `varchar(150)`  | Nome completo do município.                                                                    | — (usado para exibição/relatórios)                                          |
| `data_pagamento`   | `date`          | Data da efetivação da ordem bancária.                                                          | —                                                                           |
| `ordem_bancaria`   | `varchar(20)`   | Número da ordem bancária emitida pelo FNDE.                                                    | — (identificador financeiro único por parcela)                              |
| `valor`            | `decimal(12,2)` | Valor da ordem de pagamento (R\$).                                                             | —                                                                           |
| `parcela`          | `varchar(5)`    | Código da parcela ou tranche (ex: “1/3”, “2/2”).                                               | —                                                                           |
| `programa`         | `varchar(200)`  | Nome do programa do FNDE financiador (ex: “PDDE”, “PNAE”, “PNATE”).                            | 🔗 `fnde_data_convenio.programaNome`                                        |
| `banco`            | `varchar(100)`  | Banco onde foi depositado o recurso (ex: Banco do Brasil).                                     | —                                                                           |
| `agencia`          | `varchar(20)`   | Código da agência bancária da conta que recebeu o pagamento.                                   | —                                                                           |
| `conta_corrente`   | `varchar(30)`   | Número da conta que recebeu os valores.                                                        | —                                                                           |
| `data_extracao`    | `datetime(6)`   | Timestamp da extração do dado (carga do sistema fonte). Importante para histórico e auditoria. | —                                                                           |

🔗 Principais Relacionamentos

| Campo local        | Campo relacionado             | Tabela de referência                       | Tipo de relacionamento |
| ------------------ | ----------------------------- | ------------------------------------------ | ---------------------- |
| `municipio_codigo` | `codIbge` / `municipality_id` | `fnde_data_convenio` / `portaria_2023_07b` | Muitos para um         |
| `programa`         | `programaNome`                | `fnde_data_convenio`                       | Muitos para um         |
| `uf`               | `uf`                          | `fnde_data_escola` / `conselhos`           | Muitos para um (UF)    |


### Índices
- Index em (`id`, `ano`, `uf`, `municipio_codigo`,`municipio_nome`,`data_pagamento`,`ordem_bancaria`,`valor`,`parcela`,`programa`,`banco`,`agencia`,`conta_corrente`,`data_extracao`) conforme definido em `Meta.indexes`.