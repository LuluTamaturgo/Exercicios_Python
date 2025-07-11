🔎 Descrição da Tabela: portaria_2022_11
Esta tabela armazena os valores estimados de repasse por modalidade de ensino e os coeficientes de distribuição para os municípios em 2022, conforme os critérios definidos pela Portaria nº 11/2022. Ela está estruturada por tipo de atendimento educacional, diferenciando os valores provenientes da complementação da União via VAAT/VAAR (RP) e RC — inclusive para modalidades específicas como educação indígena, quilombola, profissional, especial e EJA.

🧩 Descrição dos Campos
| Campo                                                      | Tipo                        | Descrição                                                                                                               |
| ---------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `id`                                                       | bigint, PK, auto\_increment | Identificador único da linha na tabela.                                                                                 |
| `creche_integral_rp`                                       | decimal(8,2)                | Valor estimado para **creche em tempo integral**, referente à complementação da União na modalidade **RP (VAAT)**.      |
| `creche_parcial_rp`                                        | decimal(8,2)                | Valor estimado para **creche em tempo parcial** - modalidade **RP**.                                                    |
| `pre_escola_integral_rp`                                   | decimal(8,2)                | Valor estimado para **pré-escola em tempo integral** - modalidade **RP**.                                               |
| `pre_escola_parcial_rp`                                    | decimal(8,2)                | Valor estimado para **pré-escola em tempo parcial** - modalidade **RP**.                                                |
| `ens_fund_iniciais_urbano_rp`                              | decimal(8,2)                | Ensino Fundamental (anos iniciais) em área **urbana** - modalidade **RP**.                                              |
| `ens_fund_iniciais_rural_rp`                               | decimal(8,2)                | Ensino Fundamental (anos iniciais) em área **rural** - modalidade **RP**.                                               |
| `ens_fund_finais_urbano_rp`                                | decimal(8,2)                | Ensino Fundamental (anos finais) em área **urbana** - modalidade **RP**.                                                |
| `ens_fund_finais_rural_rp`                                 | decimal(8,2)                | Ensino Fundamental (anos finais) em área **rural** - modalidade **RP**.                                                 |
| `ens_fund_integral_rp`                                     | decimal(8,2)                | Ensino Fundamental em tempo **integral** - modalidade **RP**.                                                           |
| `ens_medio_urbano_rp`                                      | decimal(8,2)                | Ensino Médio em área **urbana** - modalidade **RP**.                                                                    |
| `ens_medio_rural_rp`                                       | decimal(8,2)                | Ensino Médio em área **rural** - modalidade **RP**.                                                                     |
| `ens_medio_integral_rp`                                    | decimal(8,2)                | Ensino Médio em tempo **integral** - modalidade **RP**.                                                                 |
| `ens_medio_integrado_prof_rp`                              | decimal(8,2)                | Ensino Médio **integrado à educação profissional** - modalidade **RP**.                                                 |
| `itinerario_formacao_tecnica_prof_rp`                      | decimal(8,2)                | **Itinerário de formação técnica e profissional** - modalidade **RP**.                                                  |
| `educacao_prof_concomitante_rp`                            | decimal(8,2)                | Educação profissional de forma **concomitante** - modalidade **RP**.                                                    |
| `educacao_especial_rp`                                     | decimal(8,2)                | Atendimentos da **educação especial** - modalidade **RP**.                                                              |
| `aee`                                                      | decimal(8,2)                | **Atendimento Educacional Especializado (AEE)** complementar à educação especial - modalidade **RP**.                   |
| `eja_avaliacao_processo_rp`                                | decimal(8,2)                | EJA com **avaliação por processo** - modalidade **RP**.                                                                 |
| `eja_integrada_profissional_rp`                            | decimal(8,2)                | EJA **integrada à educação profissional** - modalidade **RP**.                                                          |
| `educacao_indigena_quilombola_rp`                          | decimal(8,2)                | Atendimentos da **educação indígena e quilombola** - modalidade **RP**.                                                 |
| `creche_integral_rc`                                       | decimal(8,2)                | Creche em tempo integral - modalidade **RC (VAAR)**.                                                                    |
| `creche_parcial_rc`                                        | decimal(8,2)                | Creche em tempo parcial - modalidade **RC**.                                                                            |
| `pre_escola_integral_rc`                                   | decimal(8,2)                | Pré-escola em tempo integral - modalidade **RC**.                                                                       |
| `pre_escola_parcial_rc`                                    | decimal(8,2)                | Pré-escola em tempo parcial - modalidade **RC**.                                                                        |
| `educacao_especial_rc`                                     | decimal(8,2)                | Educação especial - modalidade **RC**.                                                                                  |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | decimal(8,2)                | Ensino Fundamental (finais, rural) com **formação por alternância** - modalidade **RC**.                                |
| `ens_medio_rural_rc_formacao_alternancia`                  | decimal(8,2)                | Ensino Médio rural com **formação por alternância** - RC.                                                               |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | decimal(8,2)                | Ensino Médio integrado profissional com formação por alternância - RC.                                                  |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | decimal(8,2)                | Educação indígena/quilombola com formação por alternância - RC.                                                         |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | decimal(8,2)                | EJA com avaliação por processo e formação por alternância - RC.                                                         |
| `eja_integrada_profissional_rc_formacao_alternancia`       | decimal(8,2)                | EJA integrada profissional com formação por alternância - RC.                                                           |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | decimal(8,2)                | Itinerário técnico/profissional com formação por alternância - RC.                                                      |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | decimal(8,2)                | Educação profissional concomitante com formação por alternância - RC.                                                   |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | decimal(8,2)                | Ensino Médio integrado profissional em **instituições específicas** - RC.                                               |
| `eja_integrada_profissional_rc_instituicoes_prof`          | decimal(8,2)                | EJA integrada profissional em instituições específicas - RC.                                                            |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | decimal(8,2)                | Itinerário técnico/profissional em instituições específicas - RC.                                                       |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | decimal(8,2)                | Educação profissional concomitante em instituições específicas - RC.                                                    |
| `matriculas_totais`                                        | decimal(12,2)               | Total de matrículas consideradas para os cálculos.                                                                      |
| `coeficiente_vaaf`                                         | decimal(20,12)              | **Coeficiente de distribuição VAAT/VAAR (VAAF)**, usado para ponderação no repasse de recursos do Fundeb.               |
| `estimativa_receita_vaaf`                                  | decimal(18,2)               | Estimativa da **receita total a receber** via VAAT/VAAR (valor total calculado com base nas matrículas e coeficientes). |
| `municipality_id`                                          | bigint, FK                  | Identificador do município relacionado (chave estrangeira para a tabela de municípios).                                 |

### Índices
- Index em (`id`,
`creche_integral_rp`,
`creche_parcial_rp`,
`pre_escola_integral_rp`,
`pre_escola_parcial_rp`,
`ens_fund_iniciais_urbano_rp`,
`ens_fund_iniciais_rural_rp`,
`ens_fund_finais_urbano_rp`,
`ens_fund_finais_rural_rp`,
`ens_fund_integral_rp`,
`ens_medio_urbano_rp`,
`ens_medio_rural_rp`,
`ens_medio_integral_rp`,
`ens_medio_integrado_prof_rp`,
`itinerario_formacao_tecnica_prof_rp`,
`educacao_prof_concomitante_rp`,
`educacao_especial_rp`,
`aee`,
`eja_avaliacao_processo_rp`,
`eja_integrada_profissional_rp`,
`educacao_indigena_quilombola_rp`,
`creche_integral_rc`,
`creche_parcial_rc`,
`pre_escola_integral_rc`,
`pre_escola_parcial_rc`,
`educacao_especial_rc`,
`ens_fund_finais_rural_rc_formacao_alternancia`,
`ens_medio_rural_rc_formacao_alternancia`,
`ens_medio_integrado_prof_rc_formacao_alternancia`,
`educacao_indigena_quilombola_rc_formacao_alternancia`,
`eja_avaliacao_processo_rc_formacao_alternancia`,
`eja_integrada_profissional_rc_formacao_alternancia`,
`itinerario_formacao_tecnica_prof_rc_formacao_alternancia`,
`educacao_prof_concomitante_rc_formacao_alternancia`,
`ens_medio_integrado_prof_rc_instituicoes_prof`,
`eja_integrada_profissional_rc_instituicoes_prof`,
`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,
`educacao_prof_concomitante_rc_instituicoes_prof`,
`matriculas_totais`,
`coeficiente_vaaf`,
`estimativa_receita_vaaf`,
`municipality_id`) conforme definido em `Meta.indexes`.