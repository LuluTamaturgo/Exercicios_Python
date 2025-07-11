🗂️ Tabela: fnde_data_portariadata
Essa tabela armazena os valores unitários de repasse (RP) e valores de complementação da União (RC) definidos por portarias do FNDE, por tipo de atendimento educacional. Ela consolida estimativas de receita, coeficientes de ponderação (VAAF) e o total de matrículas por município e portaria específica.

É utilizada para projeções orçamentárias, análise de financiamento da educação básica, controle de repasses e cálculo de complementações federais (como VAAT e VAAF do Fundeb).

📄 Descrição dos Campos
| Campo                                       | Tipo           | Descrição                                                                                             |
| ------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| **id**                                      | `bigint`       | Identificador único do registro. Chave primária da tabela, gerado automaticamente (`auto_increment`). |
| **creche\_integral\_rp**                    | `decimal(8,2)` | Valor do repasse por matrícula para creche em tempo integral com recurso próprio (RP).                |
| **creche\_parcial\_rp**                     | `decimal(8,2)` | Valor do repasse por matrícula para creche em tempo parcial (RP).                                     |
| **pre\_escola\_integral\_rp**               | `decimal(8,2)` | Valor do repasse por matrícula para pré-escola integral (RP).                                         |
| **pre\_escola\_parcial\_rp**                | `decimal(8,2)` | Valor do repasse por matrícula para pré-escola parcial (RP).                                          |
| **ens\_fund\_iniciais\_urbano\_rp**         | `decimal(8,2)` | Valor para ensino fundamental - anos iniciais - zona urbana (RP).                                     |
| **ens\_fund\_iniciais\_rural\_rp**          | `decimal(8,2)` | Valor para ensino fundamental - anos iniciais - zona rural (RP).                                      |
| **ens\_fund\_finais\_urbano\_rp**           | `decimal(8,2)` | Valor para ensino fundamental - anos finais - zona urbana (RP).                                       |
| **ens\_fund\_finais\_rural\_rp**            | `decimal(8,2)` | Valor para ensino fundamental - anos finais - zona rural (RP).                                        |
| **ens\_fund\_integral\_rp**                 | `decimal(8,2)` | Valor para ensino fundamental integral, independente da localização (RP).                             |
| **ens\_medio\_urbano\_rp**                  | `decimal(8,2)` | Valor para ensino médio - zona urbana (RP).                                                           |
| **ens\_medio\_rural\_rp**                   | `decimal(8,2)` | Valor para ensino médio - zona rural (RP).                                                            |
| **ens\_medio\_integral\_rp**                | `decimal(8,2)` | Valor para ensino médio integral (RP).                                                                |
| **ens\_medio\_integrado\_prof\_rp**         | `decimal(8,2)` | Valor para ensino médio integrado à educação profissional (RP).                                       |
| **itinerario\_formacao\_tecnica\_prof\_rp** | `decimal(8,2)` | Valor para itinerário formativo técnico-profissional (RP).                                            |
| **educacao\_prof\_concomitante\_rp**        | `decimal(8,2)` | Valor para educação profissional concomitante (RP).                                                   |
| **educacao\_especial\_rp**                  | `decimal(8,2)` | Valor para educação especial em classes exclusivas ou escolas especializadas (RP).                    |
| **aee**                                     | `decimal(8,2)` | Valor para Atendimento Educacional Especializado (AEE) complementar/suplementar (RP).                 |
| **eja\_avaliacao\_processo\_rp**            | `decimal(8,2)` | Valor para EJA (Educação de Jovens e Adultos) com avaliação de processo (RP).                         |
| **eja\_integrada\_profissional\_rp**        | `decimal(8,2)` | Valor para EJA integrada à educação profissional (RP).                                                |
| **educacao\_indigena\_quilombola\_rp**      | `decimal(8,2)` | Valor para educação indígena e quilombola (RP).                                                       |

🔁 Campos RC – Complementação da União:

| Campo                                                                                 | Tipo           | Descrição                                                                                         |
| ------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- |
|**creche\_integral\_rc**, 
**creche\_parcial\_rp**,
**pre\_escola\_integral\_rp**,
**pre\_escola\_parcial\_rp**,
**ens\_fund\_iniciais\_urbano\_rp**,
**ens_fund_iniciais_rural_rp**,
**ens_fund_finais_urbano_rp**,
**ens_fund_finais_rural_rp**,
**ens_fund_integral_rp**,
**ens_medio_urbano_rp**,
**ens_medio_rural_rp**,
**ens_medio_integral_rp**,
**ens_medio_integrado_prof_rp**,
**itinerario_formacao_tecnica_prof_rp **,
**educacao\_prof\_concomitante\_rc\_instituicoes\_prof** | `decimal(8,2)` | Valores de complementação da União (RC) para diferentes tipos de atendimento. Os sufixos indicam: |
|                                                                                       |                | - `_rc`: repasse de complementação direta;                                                        |
|                                                                                       |                | - `_formacao_alternancia`: atendimentos em regime de alternância (ex: escolas agrícolas);         |
|                                                                                       |                | - `_instituicoes_prof`: realizados por instituições de ensino profissional e tecnológica.         |

📊 Outros Indicadores:
| Campo                         | Tipo             | Descrição                                                                                               |
| ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------- |
| **matriculas\_totais**        | `decimal(12,2)`  | Total de matrículas registradas para os tipos de atendimento considerados.                              |
| **coeficiente\_vaaf**         | `decimal(20,12)` | Coeficiente de ponderação do VAAF (Valor Aluno Ano Fundeb). Indica quanto vale uma matrícula ponderada. |
| **estimativa\_receita\_vaaf** | `decimal(18,2)`  | Estimativa da receita total da complementação da União via VAAF para o município naquele ano/portaria.  |

🔗 Chaves Estrangeiras:
| Campo                | Tipo     | Descrição                                                                                                                       |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **municipality\_id** | `bigint` | Referência ao município. Provavelmente chave estrangeira para tabela `fnde_data_municipiofnde` ou `fnde_data_municipiosiscacs`. |
| **portaria\_id**     | `bigint` | Referência à portaria que determina os valores. Chave estrangeira para a tabela `fnde_data_portaria`.                           |

🔗 Chaves Estrangeiras / Relacionamentos

| Campo             | Tipo   | Relacionamento | Tabela Referenciada                                       | Descrição                                                     |
| ----------------- | ------ | -------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| `municipality_id` | bigint | FK (provável)  | `fnde_data_municipiofnde` ou `fnde_data_municipiosiscacs` | Referência ao município para o qual os valores são definidos. |
| `portaria_id`     | bigint | FK             | `fnde_data_portaria`                                      | Referência à portaria que determina os valores dos repasses.  |

### Índices
- Index em (`id`,`creche_integral_rp`,`creche_parcial_rp`,`pre_escola_integral_rp`,`pre_escola_parcial_rp`,`ens_fund_iniciais_urbano_rp`,`ens_fund_iniciais_rural_rp`,`ens_fund_finais_urbano_rp`,`ens_fund_finais_rural_rp`,`ens_fund_integral_rp`,`ens_medio_urbano_rp`,`ens_medio_rural_rp`,`ens_medio_integral_rp`,`ens_medio_integrado_prof_rp`,`itinerario_formacao_tecnica_prof_rp`,`educacao_prof_concomitante_rp`,`educacao_especial_rp`,`aee`,`eja_avaliacao_processo_rp`,`eja_integrada_profissional_rp`,`educacao_indigena_quilombola_rp`,`creche_integral_rc`,`creche_parcial_rc`,`pre_escola_integral_rc`,`pre_escola_parcial_rc`,
`educacao_especial_rc`,`ens_fund_finais_rural_rc_formacao_alternancia`,`ens_medio_rural_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_formacao_alternancia`,
`educacao_indigena_quilombola_rc_formacao_alternancia`,`eja_avaliacao_processo_rc_formacao_alternancia`,`eja_integrada_profissional_rc_formacao_alternancia`,
`itinerario_formacao_tecnica_prof_rc_formacao_alternancia`,`educacao_prof_concomitante_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_instituicoes_prof`,
`eja_integrada_profissional_rc_instituicoes_prof`,`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,`educacao_prof_concomitante_rc_instituicoes_prof`,
`matriculas_totais`,`coeficiente_vaaf`,`estimativa_receita_vaaf`,`municipality_id`,`portaria_id`) conforme definido em `Meta.indexes`.