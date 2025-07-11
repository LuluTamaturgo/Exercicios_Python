🗂️ Tabela fnde_data_mandatoconselho
Esta tabela registra informações detalhadas sobre cada mandato dos Conselhos Municipais de controle social dos programas do FNDE (por exemplo, CACS‑FUNDEB, Conselhos do PDDE). Cada linha corresponde a um mandato específico — isto é, ao período de atuação de uma determinada composição de conselheiros.

📑 Estrutura da Tabela



| **Campo**                    | **Tipo SQL**                 | **Descrição funcional**                                                                                             | **Relacionamento Possível**                                                                            |
| ------------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                     | `bigint` (PK)            | Identificador técnico exclusivo da linha; usado em joins e auditoria.                                           | —                                                                                                  |
| `data_cadastro`          | `datetime(6)`            | Data/hora em que o mandato foi cadastrado no sistema (timestamp de criação).                                    | —                                                                                                  |
| `mandato_conselho_id`    | `int` (UNIQUE, NOT NULL) | Código único do mandato no FNDE/SISCACS. Pode ser usado para integrar com outras tabelas oficiais ou APIs.      | —                                                                                                  |
| `conselho_id`            | `int` (FK, NOT NULL)     | Chave estrangeira que identifica o conselho responsável por este mandato.                                       | 🔗 `fnde_data_conselhomunicipal.nu_seq_conselho`                                                   |
| `data_inicio`            | `datetime(6)`            | Data de início do mandato.                                                                                      | —                                                                                                  |
| `data_termino`           | `datetime(6)`            | Data final (prevista ou efetiva) do mandato.                                                                    | —                                                                                                  |
| `quantidade_membros`     | `int`                    | Número total de conselheiros empossados neste mandato.                                                          | —                                                                                                  |
| `protocolo_mandato`      | `varchar(50)`            | Protocolo de cadastramento do mandato no SISCACS.                                                               | —                                                                                                  |
| `protocolo`              | `varchar(50)`            | Protocolo geral do processo de análise ou validação. Pode ser o mesmo do campo anterior ou um código externo.   | —                                                                                                  |
| `codigo_situacao`        | `int`                    | Código numérico da situação atual do mandato.                                                                   | —                                                                                                  |
| `descricao_situacao`     | `varchar(100)`           | Descrição textual do status do mandato (ex.: “Vigente”, “Expirado”, “Prorrogado”).                              | —                                                                                                  |
| `conselho`               | `json`                   | Bloco JSON com dados sintéticos do conselho (ex.: nome, CNPJ, tipo). Serve como snapshot informativo.           | —                                                                                                  |
| `membros`                | `json`                   | Lista em JSON com dados dos conselheiros deste mandato (ex.: nome, cargo, CPF, posse).                          | —                                                                                                  |
| `situacao_analise_grupo` | `json`                   | JSON que detalha a situação da análise por grupo de representação (governo, sociedade civil etc.).              | —                                                                                                  |
| `entidade_dirigente`     | `json`                   | Dados do dirigente da entidade (geralmente prefeito(a) ou secretário(a) de educação) envolvidos na homologação. | —                                                                                                  |
| `raw_json`               | `json` (NOT NULL)        | Bloco JSON original recebido da API do FNDE. Serve para auditoria e verificação da integridade dos dados.       | —                                                                                                  |
| `municipality_id`        | `bigint` (FK, NOT NULL)  | Chave estrangeira para o município relacionado ao conselho. Indexado para acelerar filtros regionais.           | 🔗 `fnde_data_conselhomunicipal.municipality_id`<br>🔗 `fnde_data_informacoesibge.municipality_id` |

🔗 Principais Relacionamentos

| Campo local       | Campo relacionado | Tabela relacionada                                             | Tipo           |
| ----------------- | ----------------- | -------------------------------------------------------------- | -------------- |
| `conselho_id`     | `nu_seq_conselho` | `fnde_data_conselhomunicipal`                                  | Muitos para Um |
| `municipality_id` | `id`              | `fnde_data_cnpjmunicipio`<br>ou<br>`fnde_data_informacoesibge` | Muitos para Um |

Importante: conselho_id se refere diretamente à tabela de conselhos (fnde_data_conselhomunicipal) por meio do campo nu_seq_conselho, enquanto municipality_id pode se referir à tabela de municípios base, como fnde_data_informacoesibge ou similar.

### Índices
- Index em (`id`,`data_cadastro`,`mandato_conselho_id`,`conselho_id`,`data_inicio`,`data_termino`,`quantidade_membros`,`protocolo_mandato`,`protocolo`,`codigo_situacao`,`descricao_situacao`,`conselho`,`membros`,`situacao_analise_grupo`,`entidade_dirigente`,`raw_json`,`municipality_id`) conforme definido em `Meta.indexes`.