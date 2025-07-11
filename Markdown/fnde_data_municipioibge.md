Tabela: fnde_data_municipioibge
Essa tabela contém dados básicos e padronizados dos municípios brasileiros conforme o Instituto Brasileiro de Geografia e Estatística (IBGE). Ela serve como referência oficial para identificar municípios por código e nome, e é fundamental para integrar bases de dados públicas, especialmente na área da educação e gestão pública.

| **Campo**    | **Tipo**         | **Obrigatório / Restrição**       | **Descrição funcional**                                                                                  | **Relacionamentos possíveis**                                                               |
| -------- | ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`     | bigint       | PK, NOT NULL, auto\_increment | Identificador único da linha; chave primária para consultas e relacionamentos.                       | —                                                                                       |
| `codigo` | varchar(7)   | NOT NULL, UNIQUE              | Código oficial do município segundo padrão IBGE (7 dígitos). Usado para integração com outras bases. | Relaciona-se com `municipio_codigo` de outras tabelas FNDE e com o código IBGE externo. |
| `nome`   | varchar(100) | NOT NULL                      | Nome oficial do município (ex: "Fortaleza", "Curitiba"). Usado para exibição e organização textual.  | —                                                                                       |
| `uf`     | varchar(2)   | NOT NULL                      | Sigla da Unidade Federativa (ex: "SP", "MG", "BA"). Útil para agrupamento e filtros por estado.      | —                                                                                       |

🔗 Possíveis Relacionamentos

| **Tabela Relacionada**                       | **Campo FK nesta tabela** | **Campo Referenciado**                                       | **Observações**                                     |
| ---------------------------------------- | --------------------- | -------------------------------------------------------- | ------------------------------------------------- |
| Outras tabelas FNDE que usam código IBGE | `codigo`              | Campos correspondentes (`municipio_codigo`, `ibge_code`) | Integração geográfica e padronização entre bases. |

## Resumo

Essa tabela é a referência oficial do IBGE para municípios, contendo código padronizado, nome e estado.

O campo codigo é essencial para garantir a integridade e unicidade dos municípios em diversas integrações e análises.

Serve de base para cruzar dados com outras tabelas do FNDE e fontes externas.

Auxilia na padronização de relatórios, filtros e análises por estado e município.
### Índices
- Index em (`id`,`codigo`,`nome`,`uf`) conforme definido em `Meta.indexes`.