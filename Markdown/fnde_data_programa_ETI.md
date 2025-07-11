Tabela: fnde_data_programa_ETI
A tabela fnde_data_programa_ETI armazena informações financeiras sobre repasses realizados pelo FNDE ao município no contexto do Programa Educação e Tecnologia da Informação (ETI) ou programas correlatos com mesma natureza. Registra valores pagos, dados bancários, e detalhes da parcela repassada, permitindo rastreamento e fiscalização dos recursos públicos.

| Campo                 | Tipo            | Obrigatório | Observações                                                                                                                      |
| --------------------- | --------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **id**                | `bigint`        | Sim (PK)    | Identificador único do registro na tabela. Gerado automaticamente (`auto_increment`).                                            |
| **ano**               | `int`           | Sim         | Ano de referência do repasse ou exercício orçamentário em que ocorreu o pagamento.                                               |
| **uf**                | `varchar(2)`    | Sim         | Sigla da Unidade Federativa (ex: "SP", "BA", "MG"). Permite filtrar os dados por estado.                                         |
| **municipio\_codigo** | `varchar(20)`   | Sim         | Código único do município (possivelmente padrão IBGE ou FNDE). Usado para identificar formalmente o ente federado.               |
| **municipio\_nome**   | `varchar(200)`  | Sim         | Nome completo do município beneficiado com o repasse.                                                                            |
| **data\_pagamento**   | `date`          | Sim         | Data em que o valor foi efetivamente pago ao município. Importante para controle e auditoria.                                    |
| **ordem\_bancaria**   | `varchar(100)`  | Sim         | Identificador da ordem bancária emitida pelo FNDE. Pode ser usada para rastreamento no SIAFI ou SIOPE.                           |
| **valor**             | `decimal(15,2)` | Sim         | Valor financeiro transferido para o município naquela parcela.                                                                   |
| **parcela**           | `varchar(50)`   | Sim         | Número ou descrição da parcela (ex: "1ª parcela", "única", "parcela complementar"). Útil para gestão de cronograma de repasses.  |
| **programa**          | `varchar(100)`  | Sim         | Nome do programa ou ação específica do FNDE ao qual o repasse está vinculado (ex: ETI, PDDE, PNATE).                             |
| **banco**             | `varchar(100)`  | Sim         | Nome do banco onde os recursos foram depositados.                                                                                |
| **agencia**           | `varchar(100)`  | Sim         | Código da agência bancária responsável pelo recebimento.                                                                         |
| **conta\_corrente**   | `varchar(100)`  | Sim         | Número da conta corrente onde o recurso foi creditado. Importante para conferência bancária.                                     |
| **data\_extracao**    | `datetime(6)`   | Sim         | Data e hora da extração dos dados do sistema de origem. Usada para rastrear atualizações e garantir a integridade da informação. |

🔗 Possíveis Relacionamentos
O campo municipio_codigo pode ser relacionado a tabelas padrão de municípios, como fnde_data_municipiofnde, fnde_data_municipiosiscacs ou fnde_data_municipioibge, para garantir integridade e padronização dos dados geográficos.

O campo programa pode ser cruzado com tabelas que contenham listagem e detalhes dos programas do FNDE, para padronização de nomenclatura e vinculação.

Campos bancários (banco, agencia, conta_corrente) são usados para conferência e auditoria, mas normalmente não relacionam com outras tabelas diretamente.

### Índices
- Index em (`id`,`ano`,`uf`,`municipio_codigo`,`municipio_nome`,`data_pagamento`,`ordem_bancaria`,`valor`,`parcela`,`programa`,`banco`,`agencia`,`conta_corrente`,
`data_extracao`,) conforme definido em `Meta.indexes`.