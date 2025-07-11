🗂️ Tabela fnde_data_fndeprogramassigpc
Esta tabela sintetiza informações que o Sistema de Gestão de Prestação de Contas (SIGPC) publica sobre a situação das prestações de contas dos programas do FNDE — inclusive eventuais pedidos de complementação (“OPC”), medidas de exceção e efeitos suspensivos aplicados a cada entidade.

| Campo               | Tipo SQL       | Descrição funcional                                                                                                                                | Relacionamento Possível                                                          |
| ------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                | `bigint` (PK)  | Identificador único da linha na tabela. Usado para auditoria e controle de integridade.                                                            | —                                                                                |
| `tipo_opc`          | `varchar(50)`  | Tipo de Pedido de Complementação (**OPC**) registrado (ex: "Recurso", "Reanálise", "Complementação"). Se não houver, aparece como “Sem pendência”. | —                                                                                |
| `ano`               | `int`          | Ano de referência da prestação de contas. Pode ou não coincidir com o ano do repasse.                                                              | 🔗 `fnde_data_fndeprogramas.ano`                                                 |
| `ciclo`             | `varchar(20)`  | Nome do ciclo (ex: “1º Ciclo”, “Extraordinário 2021”). Pode haver mais de um ciclo por ano.                                                        | —                                                                                |
| `programa`          | `varchar(100)` | Nome do programa analisado (ex: PNAE, PDDE, PNATE).                                                                                                | 🔗 `fnde_data_fndeprogramas.programa`<br>🔗 `fnde_data_convenio.programaNome`    |
| `uf`                | `varchar(2)`   | Sigla da unidade federativa da entidade prestadora de contas.                                                                                      | 🔗 `fnde_data_convenio.ufNome`<br>🔗 `fnde_data_escola.uf`                       |
| `entidade`          | `varchar(150)` | Nome da entidade responsável pela prestação de contas (prefeitura, escola, secretaria etc.).                                                       | 🔗 `fnde_data_convenio.entidadeNome`                                             |
| `fase`              | `varchar(100)` | Etapa atual da análise da prestação de contas (ex: “Em complementação”, “Aprovada”).                                                               | 🔗 `fnde_data_convenio.faseNome`                                                 |
| `situacao_pc`       | `varchar(50)`  | Situação consolidada da prestação (geralmente similar à fase, mas em forma padronizada).                                                           | 🔗 `fnde_data_convenio.situacaoPCNome`                                           |
| `situacao_opc`      | `varchar(50)`  | Situação do pedido de complementação: “Aberto”, “Respondido”, “Encerrado”, ou “Sem OPC”.                                                           | —                                                                                |
| `medida_excecao`    | `varchar(100)` | Medida excepcional registrada pelo FNDE (ex: “Prorrogação”, “Aceite parcial”).                                                                     | 🔗 `fnde_data_convenio.medidaExcecao`                                            |
| `efeito_suspensivo` | `varchar(100)` | Justificativa de bloqueio ou impedimento da prestação de contas.                                                                                   | 🔗 `fnde_data_convenio.efeitoSuspensivo`                                         |
| `municipio_id`      | `varchar(10)`  | Código IBGE do município da entidade. Pode ser nulo se for órgão estadual/federal.                                                                 | 🔗 `fnde_data_fndeprogramas.municipio_codigo`<br>🔗 `fnde_data_convenio.codIbge` |
| `data_atualizacao`  | `datetime(6)`  | Data e hora da última coleta do SIGPC (serve para verificar atualidade dos dados).                                                                 | —                                                                                |

🔗 Relacionamentos Identificados

| Campo local         | Campo relacionado              | Tabela relacionada                              | Tipo           |
| ------------------- | ------------------------------ | ----------------------------------------------- | -------------- |
| `programa`          | `programa`, `programaNome`     | `fnde_data_fndeprogramas`, `fnde_data_convenio` | Muitos para um |
| `uf`                | `uf`, `ufNome`                 | `fnde_data_convenio`, `fnde_data_escola`        | Muitos para um |
| `entidade`          | `entidadeNome`                 | `fnde_data_convenio`                            | Muitos para um |
| `fase`              | `faseNome`                     | `fnde_data_convenio`                            | Muitos para um |
| `situacao_pc`       | `situacaoPCNome`               | `fnde_data_convenio`                            | Muitos para um |
| `medida_excecao`    | `medidaExcecao`                | `fnde_data_convenio`                            | Muitos para um |
| `efeito_suspensivo` | `efeitoSuspensivo`             | `fnde_data_convenio`                            | Muitos para um |
| `municipio_id`      | `municipio_codigo` / `codIbge` | `fnde_data_fndeprogramas`, `fnde_data_convenio` | Muitos para um |


### Índices
- Index em (`id`, `tipo_opc`, `ano`, `ciclo`,`programa`,`uf`,`entidade`,`fase`,`situacao_pc`,`situacao_opc`,`medida_excecao`,`efeito_suspensivo`,`municipio_id`,`data_atualizacao`) conforme definido em `Meta.indexes`.