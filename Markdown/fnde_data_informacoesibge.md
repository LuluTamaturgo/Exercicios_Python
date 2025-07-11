🗂️ Tabela fnde_data_informacoesibge
Esta tabela consolida indicadores demográficos, sociais e econômicos do IBGE para cada município, servindo como fonte de contexto para análises de programas do FNDE (per capita, priorização de recursos, estudos de impacto).

| **Campo**                        | **Tipo SQL**             | **Descrição funcional**                                                                                              | **Relacionamento Possível**                                                             |
| ----------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                          | `bigint` (PK)         | Identificador técnico da linha. Usado para auditoria e rastreabilidade.                                          | —                                                                                   |
| `populacao_estimada`          | `int`                 | População estimada do município no ano (`populacao_ano`). Valor publicado pelo IBGE.                             | —                                                                                   |
| `populacao_ano`               | `varchar(4)`          | Ano da estimativa populacional (ex.: "2024").                                                                    | —                                                                                   |
| `atualizado_em`               | `datetime(6)`         | Data e hora da última atualização do registro no banco. Serve para controle de versão dos dados.                 | —                                                                                   |
| `municipality_id`             | `bigint` (UNIQUE, FK) | Chave estrangeira que referencia a tabela de municípios. Garante um único conjunto de indicadores por município. | 🔗 `fnde_data_cnpjmunicipio.id`<br>🔗 `fnde_data_conselhomunicipal.municipality_id` |
| `area_territorial_km2`        | `decimal(10,2)`       | Área territorial total do município, em km².                                                                     | —                                                                                   |
| `densidade_demografica`       | `decimal(10,2)`       | Habitantes por km². Calculado a partir da população estimada e área territorial.                                 | —                                                                                   |
| `expectativa_vida`            | `decimal(5,2)`        | Expectativa de vida ao nascer (em anos).                                                                         | —                                                                                   |
| `indice_envelhecimento`       | `decimal(6,2)`        | Relação percentual entre população ≥ 60 anos e ≤ 14 anos. Indica o grau de envelhecimento populacional.          | —                                                                                   |
| `indice_gini`                 | `decimal(4,3)`        | Índice de Gini da renda domiciliar per capita. Varia de 0 (igualdade) a 1 (desigualdade máxima).                 | —                                                                                   |
| `pib_per_capita`              | `decimal(12,2)`       | PIB per capita municipal, em reais correntes.                                                                    | —                                                                                   |
| `rendimento_medio_domiciliar` | `decimal(12,2)`       | Renda domiciliar per capita mensal, em reais.                                                                    | —                                                                                   |
| `taxa_analfabetismo_15_mais`  | `decimal(5,2)`        | Taxa de analfabetismo da população com 15 anos ou mais, em %.                                                    | —                                                                                   |
| `taxa_urbanizacao`            | `decimal(5,2)`        | Percentual da população vivendo em áreas urbanas.                                                                | —                                                                                   |

🔗 Relacionamento Chave

| Campo local       | Campo relacionado | Tabela relacionada            | Tipo       |
| ----------------- | ----------------- | ----------------------------- | ---------- |
| `municipality_id` | `id`              | `fnde_data_cnpjmunicipio`     | Um para um |
| `municipality_id` | `municipality_id` | `fnde_data_conselhomunicipal` | Um para um |

Nota: Se o sistema tiver uma tabela de municípios centralizada (como fnde_data_municipiofnde), o campo municipality_id pode se referir a ela também

### Índices
- Index em (`id`,`populacao_estimada`,`populacao_ano`,`atualizado_em`,`municipality_id`,`area_territorial_km2`,`densidade_demografica`,`expectativa_vida`,`indice_envelhecimento`,`indice_gini`,`pib_per_capita`,`rendimento_medio_domiciliar`,`taxa_analfabetismo_15_mais`,`taxa_urbanizacao`) conforme definido em `Meta.indexes`.













