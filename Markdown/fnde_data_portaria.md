Tabela: fnde_data_portaria
A tabela fnde_data_portaria armazena informações sobre portarias publicadas pelo FNDE (Fundo Nacional de Desenvolvimento da Educação). Portarias são documentos oficiais que regulamentam, autorizam, ou instruem ações administrativas, normativas ou financeiras relacionadas a programas, repasses e ações do FNDE.

Essa tabela é útil para fins de controle, auditoria, consulta normativa e vinculação com outras informações operacionais.

| Campo                | Tipo de dado   | Obrigatório    | Observações                                                                                                                                    |
| -------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **id**               | `bigint`       | Sim (NOT NULL) | Chave primária da tabela, gerada automaticamente (`auto_increment`). Identifica unicamente cada portaria registrada.                           |
| **numero**           | `varchar(100)` | Sim            | Número oficial da portaria (ex: "Portaria nº 123/2023"). Pode incluir ano ou tipo de portaria.                                                 |
| **data\_publicacao** | `date`         | Não            | Data em que a portaria foi oficialmente publicada. Essencial para controle legal e histórico.                                                  |
| **ano\_base**        | `int`          | Sim            | Ano de referência a que a portaria se aplica (ex: ano da vigência de recursos, programas ou normas). Pode ser diferente da data de publicação. |
| **descricao**        | `longtext`     | Não            | Texto completo ou resumo da portaria. Pode conter seu conteúdo normativo, instruções, objetivos e determinações.                               |

## Observações gerais

Essa tabela é útil para controle normativo e auditoria.

Pode ser vinculada indiretamente a outras tabelas que usem normas ou portarias para validar ou justificar dados e processos.

O campo ano_base pode ser utilizado para relacionar portarias a exercícios financeiros ou programas de determinado ano.

### Índices
- Index em (`id`,`numero`,`data_publicacao`,`ano_base`,`descricao`) conforme definido em `Meta.indexes`.