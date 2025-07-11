tabela fnde_data_programa_PNATE
A tabela armazena o histórico de pagamentos do FNDE referentes ao Programa Nacional de Apoio ao Transporte do Escolar (PNATE).
Cada linha representa uma ordem bancária liberada para determinada entidade municipal em um ano e parcela específicos. O objetivo é permitir rastrear, auditar e consolidar os repasses efetuados, bem como cruzá‑los com dados contábeis, prestações de contas e indicadores de transporte escolar.

| Coluna             | Tipo / Restrições                            | Descrição funcional                                                                                                                                          |
| ------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`               | **bigint** • PK • auto\_increment • NOT NULL | Identificador técnico exclusivo da linha (surrogate key). Facilita integrações internas sem depender de códigos externos.                                    |
| `ano`              | **int** • NOT NULL                           | Exercício financeiro a que a ordem bancária se refere (ex.: 2024). Permite análises por exercício e consolidações anuais.                                    |
| `uf`               | **varchar(2)** • NOT NULL                    | Unidade federativa (sigla em padrão IBGE, ex.: “BA”). Útil para filtros regionais e construção de painéis por estado.                                        |
| `municipio_codigo` | **varchar(20)** • NOT NULL                   | Código IBGE do município beneficiário. Serve de chave de integração com cadastros territoriais e com as tabelas‐espelho de municípios.                       |
| `municipio_nome`   | **varchar(200)** • NOT NULL                  | Nome oficial do município (ex.: “Salvador”). Armazena redundância desnormalizada para consultas sem junções externas e para exibição direta.                 |
| `data_pagamento`   | **date** • NOT NULL                          | Data em que o FNDE efetivou a ordem bancária (liquidação). Permite auditoria de prazos entre empenho × liquidação × prestação.                               |
| `ordem_bancaria`   | **varchar(100)** • NOT NULL                  | Número ou código da ordem bancária emitida pelo FNDE/SIAFI. Associado a comprovantes de transferência no extrato bancário.                                   |
| `valor`            | **decimal(15,2)** • NOT NULL                 | Valor creditado em reais (R\$). Precisão de 2 casas decimais e até 999 999 999 999 999,99 R\$. Essencial para cálculos de total repassado por ano/parcela.   |
| `parcela`          | **varchar(50)** • NOT NULL                   | Identifica a parcela ou quota do exercício (ex.: “Parcela Única”, “1ª Parcela”). Viabiliza conferência de calendário de liberações.                          |
| `programa`         | **varchar(100)** • NOT NULL                  | Nome do programa de financiamento. No contexto desta tabela, normalmente “PNATE”, mas mantém‑se genérico para possíveis variações ou fusões de programas.    |
| `banco`            | **varchar(100)** • NOT NULL                  | Banco onde o crédito foi efetuado (ex.: “Banco do Brasil”). Auxilia na conciliação bancária e identificação de regras de TED/PIX.                            |
| `agencia`          | **varchar(100)** • NOT NULL                  | Agência do banco destinatário. Importante para identificar eventual necessidade de atualização cadastral.                                                    |
| `conta_corrente`   | **varchar(100)** • NOT NULL                  | Número da conta corrente beneficiária. Fundamental em auditorias antifraude e no rastreio de devoluções.                                                     |
| `data_extracao`    | **datetime(6)** • NOT NULL                   | Timestamp (até microssegundos) de quando a informação foi extraída do sistema‐fonte. Essencial para controle de versões, rebuilds de data lake e SCD‑Type 2. |

🔗 Possíveis relacionamentos
municipio_codigo pode ser referenciado em tabelas municipais padronizadas (ex: fnde_data_municipiofnde, fnde_data_municipiosiscacs) para garantir consistência.

programa geralmente será "PNATE", mas o campo flexível permite possíveis adaptações.

Campos bancários (banco, agencia, conta_corrente) são importantes para auditoria e podem ser cruzados com dados financeiros externos.

### Índices
- Index em (`id`,`ano`,`uf`,`municipio_codigo`,`municipio_nome`,`data_pagamento`,`ordem_bancaria`,`valor`,`parcela`,`programa`,`banco`,`agencia`,`conta_corrente`,
`data_extracao` ) conforme definido em `Meta.indexes`.