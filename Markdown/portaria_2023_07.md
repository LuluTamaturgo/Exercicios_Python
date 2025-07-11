# 🗂️ Descrição da Tabela: portaria_2023_07
A tabela portaria_2023_07 armazena os valores estimados por matrícula utilizados para o cálculo da complementação da União ao Fundeb, conforme definido pela Portaria Interministerial nº 7/2023. Esses valores estão segmentados pelas modalidades de ensino, tipo de repasse — RP (VAAT) e RC (VAAR) —, e categorias específicas como educação especial, educação profissional, EJA, e formação por alternância. A tabela também inclui o total de matrículas, o coeficiente VAAT/VAAR e a estimativa de receita federal para cada município.

| Campo                                                      | Tipo           | Descrição                                                                |
| ---------------------------------------------------------- | -------------- | ------------------------------------------------------------------------ |
| `id`                                                       | bigint         | Identificador único da linha na tabela (chave primária, auto increment). |
| `creche_integral_rp`                                       | decimal(8,2)   | Valor estimado para creche integral - modalidade **RP (VAAT)**.          |
| `creche_parcial_rp`                                        | decimal(8,2)   | Valor estimado para creche parcial - RP.                                 |
| `pre_escola_integral_rp`                                   | decimal(8,2)   | Pré-escola integral - RP.                                                |
| `pre_escola_parcial_rp`                                    | decimal(8,2)   | Pré-escola parcial - RP.                                                 |
| `ens_fund_iniciais_urbano_rp`                              | decimal(8,2)   | Ens. Fund. anos iniciais - urbano - RP.                                  |
| `ens_fund_iniciais_rural_rp`                               | decimal(8,2)   | Ens. Fund. anos iniciais - rural - RP.                                   |
| `ens_fund_finais_urbano_rp`                                | decimal(8,2)   | Ens. Fund. anos finais - urbano - RP.                                    |
| `ens_fund_finais_rural_rp`                                 | decimal(8,2)   | Ens. Fund. anos finais - rural - RP.                                     |
| `ens_fund_integral_rp`                                     | decimal(8,2)   | Ens. Fund. em tempo integral - RP.                                       |
| `ens_medio_urbano_rp`                                      | decimal(8,2)   | Ensino Médio - urbano - RP.                                              |
| `ens_medio_rural_rp`                                       | decimal(8,2)   | Ensino Médio - rural - RP.                                               |
| `ens_medio_integral_rp`                                    | decimal(8,2)   | Ensino Médio integral - RP.                                              |
| `ens_medio_integrado_prof_rp`                              | decimal(8,2)   | Ens. Médio integrado à ed. profissional - RP.                            |
| `itinerario_formacao_tecnica_prof_rp`                      | decimal(8,2)   | Itinerário técnico/profissional - RP.                                    |
| `educacao_prof_concomitante_rp`                            | decimal(8,2)   | Educação profissional concomitante - RP.                                 |
| `educacao_especial_rp`                                     | decimal(8,2)   | Educação especial - RP.                                                  |
| `aee`                                                      | decimal(8,2)   | Atendimento Educacional Especializado - RP.                              |
| `eja_avaliacao_processo_rp`                                | decimal(8,2)   | EJA com avaliação por processo - RP.                                     |
| `eja_integrada_profissional_rp`                            | decimal(8,2)   | EJA integrada à ed. profissional - RP.                                   |
| `educacao_indigena_quilombola_rp`                          | decimal(8,2)   | Educação indígena/quilombola - RP.                                       |
| `creche_integral_rc`                                       | decimal(8,2)   | Creche integral - modalidade **RC (VAAR)**.                              |
| `creche_parcial_rc`                                        | decimal(8,2)   | Creche parcial - RC.                                                     |
| `pre_escola_integral_rc`                                   | decimal(8,2)   | Pré-escola integral - RC.                                                |
| `pre_escola_parcial_rc`                                    | decimal(8,2)   | Pré-escola parcial - RC.                                                 |
| `educacao_especial_rc`                                     | decimal(8,2)   | Educação especial - RC.                                                  |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | decimal(8,2)   | Ens. Fund. finais, rural, com formação por alternância - RC.             |
| `ens_medio_rural_rc_formacao_alternancia`                  | decimal(8,2)   | Ens. Médio rural com formação por alternância - RC.                      |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | decimal(8,2)   | Ens. Médio integrado prof. com alternância - RC.                         |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | decimal(8,2)   | Educação indígena/quilombola com alternância - RC.                       |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | decimal(8,2)   | EJA com avaliação por processo e alternância - RC.                       |
| `eja_integrada_profissional_rc_formacao_alternancia`       | decimal(8,2)   | EJA integrada profissional com alternância - RC.                         |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | decimal(8,2)   | Itinerário técnico/profissional com alternância - RC.                    |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | decimal(8,2)   | Educação profissional concomitante com alternância - RC.                 |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | decimal(8,2)   | Ens. Médio integrado prof. em instituições específicas - RC.             |
| `eja_integrada_profissional_rc_instituicoes_prof`          | decimal(8,2)   | EJA integrada profissional em instituições específicas - RC.             |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | decimal(8,2)   | Itinerário técnico/profissional em instituições específicas - RC.        |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | decimal(8,2)   | Educação prof. concomitante em instituições específicas - RC.            |
| `matriculas_totais`                                        | decimal(12,2)  | Total de matrículas consideradas para os cálculos.                       |
| `coeficiente_vaaf`                                         | decimal(20,12) | Coeficiente de ponderação VAAT/VAAR (VAAF).                              |
| `estimativa_receita_vaaf`                                  | decimal(18,2)  | Estimativa de receita da União via complementação.                       |
| `municipality_id`                                          | bigint         | Identificador do município (chave estrangeira).                          |

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
`ens_medio_integral_rp`,`,
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