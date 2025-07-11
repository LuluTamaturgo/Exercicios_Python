A tabela fnde_data_municipiosiscacs reúne informações cadastrais e territoriais padronizadas dos municípios brasileiros com foco na interoperabilidade entre sistemas federais, especialmente os que envolvem gestão educacional e repasses do FNDE (como o sistema SISCACS, usado por Conselhos de Acompanhamento e Controle Social do Fundeb).

Ela consolida códigos oficiais de diferentes órgãos — como IBGE, FNDE, Correios, INSS, SIAFI — para um mesmo município, permitindo cruzamento seguro e automatizado de dados públicos.

Tabela: fnde_data_municipiosiscacs
Esta tabela atua como uma base integradora de municípios, usada para garantir que todos os sistemas do governo se referenciem a um mesmo município por meio de múltiplos identificadores oficiais.

É muito útil para aplicações que cruzam dados de diversos sistemas federais, como repasses financeiros, controle social, ou auditorias.

🔍 Descrição dos Campos

| **Campo**                        | **Tipo**         | **Obrigatório / Restrição**       | **Descrição funcional**                                                                                                    | **Relacionamentos possíveis**                           |
| ---------------------------- | ------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `id`                         | bigint       | PK, NOT NULL, auto\_increment | Identificador único do registro; chave primária da tabela.                                                             | —                                                   |
| `co_municipio_fnde`          | varchar(10)  | NOT NULL, UNIQUE              | Código do município usado pelo FNDE. Identificador principal para programas do FNDE (ex.: PDDE, Fundeb).               | Relaciona-se a outros dados do FNDE via código FNDE |
| `co_municipio_ibge`          | varchar(10)  | NULL                          | Código do município conforme padrão IBGE. Facilita integração com bases estatísticas e educacionais oficiais.          | Relaciona-se à tabela `fnde_data_municipioibge`     |
| `no_municipio`               | varchar(255) | NOT NULL                      | Nome oficial completo do município.                                                                                    | —                                                   |
| `sg_uf`                      | varchar(2)   | NOT NULL                      | Sigla da unidade federativa (estado). Permite agrupamento por estado.                                                  | —                                                   |
| `nu_cep_municipio`           | varchar(10)  | NULL                          | CEP principal do município, para correspondências e validações.                                                        | —                                                   |
| `co_municipio_correio`       | varchar(10)  | NULL                          | Código do município segundo os Correios, usado em integrações postais.                                                 | —                                                   |
| `co_municipio_inss`          | varchar(10)  | NULL                          | Código utilizado pelo INSS para identificação do município.                                                            | —                                                   |
| `co_municipio_siafi`         | varchar(10)  | NULL                          | Código do município no sistema SIAFI, usado em transferências financeiras da União.                                    | —                                                   |
| `co_microregiao_ibge`        | varchar(10)  | NULL                          | Código da microrregião IBGE, agrupamento intermediário regional.                                                       | —                                                   |
| `co_mesoregiao_ibge`         | varchar(10)  | NULL                          | Código da mesorregião IBGE, agrupamento mais amplo para análises regionais e censitárias.                              | —                                                   |
| `co_municipio_ibge_completo` | varchar(20)  | NULL                          | Código IBGE estendido ou customizado (ex.: IBGE + UF) para casos especiais de cruzamento.                              | —                                                   |
| `atualizado_em`              | datetime(6)  | NOT NULL                      | Timestamp da última atualização do registro. Essencial para controle de versões e sincronização com sistemas externos. | —                                                   |

🔗 Possíveis Relacionamentos e Integrações

| **Tabela Relacionada**                                            | **Campo FK nesta tabela** | **Campo Referenciado**    | **Observações**                                                     |
| ------------------------------------------------------------- | --------------------- | --------------------- | --------------------------------------------------------------- |
| `fnde_data_municipioibge`                                     | `co_municipio_ibge`   | `codigo`              | Código IBGE padrão para cruzar dados oficiais do IBGE.          |
| Outras tabelas FNDE (programas, conselhos, escolas, repasses) | `co_municipio_fnde`   | Código municipal FNDE | Integração e cruzamento interno das bases FNDE com esse código. |

## Resumo
A tabela atua como hub que centraliza múltiplos identificadores oficiais para municípios.

Facilita a interoperabilidade entre diferentes sistemas federais e bases de dados.

Crucial para garantir precisão no cruzamento e integração de dados municipais em diferentes órgãos e sistemas.

Campos adicionais (Correios, INSS, SIAFI) ampliam a abrangência e a utilidade da base.

### Índices
- Index em (`id`,`co_municipio_fnde`,`co_municipio_ibge`,`no_municipio`,`sg_uf`,`nu_cep_municipio`,`co_municipio_correio`,`co_municipio_inss`,`co_municipio_siafi`,`co_microregiao_ibge`,`co_mesoregiao_ibge`,`co_municipio_ibge_completo`,`atualizado_em`) conforme definido em `Meta.indexes`.