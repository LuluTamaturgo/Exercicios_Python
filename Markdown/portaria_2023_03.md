# 🗂️ Descrição da Tabela: portaria_2023_03
A tabela portaria_2023_03 contém os valores estimados de repasse por modalidade de ensino e os coeficientes utilizados para distribuição de recursos federais do Fundeb aos municípios no exercício de 2023, conforme a Portaria Interministerial nº 3/2023. Os dados diferenciam os valores da complementação da União por tipo de repasse: RP (VAAT) e RC (VAAR), considerando também modalidades específicas como educação especial, educação indígena/quilombola, educação profissional, EJA e formação por alternância.

🧩 Descrição dos Campos
| Campo                                                      | Tipo                        | Descrição                                                                   |
| ---------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------- |
| `id`                                                       | bigint, PK, auto\_increment | Identificador único da linha na tabela.                                     |
| `creche_integral_rp`                                       | decimal(8,2)                | Valor estimado para creche em tempo integral, modalidade **RP (VAAT)**.     |
| `creche_parcial_rp`                                        | decimal(8,2)                | Valor estimado para creche em tempo parcial - RP.                           |
| `pre_escola_integral_rp`                                   | decimal(8,2)                | Valor estimado para pré-escola em tempo integral - RP.                      |
| `pre_escola_parcial_rp`                                    | decimal(8,2)                | Valor estimado para pré-escola em tempo parcial - RP.                       |
| `ens_fund_iniciais_urbano_rp`                              | decimal(8,2)                | Ensino Fundamental (anos iniciais) urbano - RP.                             |
| `ens_fund_iniciais_rural_rp`                               | decimal(8,2)                | Ensino Fundamental (anos iniciais) rural - RP.                              |
| `ens_fund_finais_urbano_rp`                                | decimal(8,2)                | Ensino Fundamental (anos finais) urbano - RP.                               |
| `ens_fund_finais_rural_rp`                                 | decimal(8,2)                | Ensino Fundamental (anos finais) rural - RP.                                |
| `ens_fund_integral_rp`                                     | decimal(8,2)                | Ensino Fundamental em tempo integral - RP.                                  |
| `ens_medio_urbano_rp`                                      | decimal(8,2)                | Ensino Médio urbano - RP.                                                   |
| `ens_medio_rural_rp`                                       | decimal(8,2)                | Ensino Médio rural - RP.                                                    |
| `ens_medio_integral_rp`                                    | decimal(8,2)                | Ensino Médio em tempo integral - RP.                                        |
| `ens_medio_integrado_prof_rp`                              | decimal(8,2)                | Ensino Médio integrado à educação profissional - RP.                        |
| `itinerario_formacao_tecnica_prof_rp`                      | decimal(8,2)                | Itinerário de formação técnica e profissional - RP.                         |
| `educacao_prof_concomitante_rp`                            | decimal(8,2)                | Educação profissional concomitante - RP.                                    |
| `educacao_especial_rp`                                     | decimal(8,2)                | Educação especial - RP.                                                     |
| `aee`                                                      | decimal(8,2)                | Atendimento Educacional Especializado (AEE) - RP.                           |
| `eja_avaliacao_processo_rp`                                | decimal(8,2)                | EJA com avaliação por processo - RP.                                        |
| `eja_integrada_profissional_rp`                            | decimal(8,2)                | EJA integrada à educação profissional - RP.                                 |
| `educacao_indigena_quilombola_rp`                          | decimal(8,2)                | Educação indígena e quilombola - RP.                                        |
| `creche_integral_rc`                                       | decimal(8,2)                | Creche em tempo integral - **RC (VAAR)**.                                   |
| `creche_parcial_rc`                                        | decimal(8,2)                | Creche em tempo parcial - RC.                                               |
| `pre_escola_integral_rc`                                   | decimal(8,2)                | Pré-escola em tempo integral - RC.                                          |
| `pre_escola_parcial_rc`                                    | decimal(8,2)                | Pré-escola em tempo parcial - RC.                                           |
| `educacao_especial_rc`                                     | decimal(8,2)                | Educação especial - RC.                                                     |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | decimal(8,2)                | Ens. Fund. (finais, rural) com formação por alternância - RC.               |
| `ens_medio_rural_rc_formacao_alternancia`                  | decimal(8,2)                | Ens. Médio rural com formação por alternância - RC.                         |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | decimal(8,2)                | Ens. Médio integrado profissional com formação por alternância - RC.        |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | decimal(8,2)                | Educação indígena/quilombola com formação por alternância - RC.             |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | decimal(8,2)                | EJA com avaliação por processo e formação por alternância - RC.             |
| `eja_integrada_profissional_rc_formacao_alternancia`       | decimal(8,2)                | EJA integrada profissional com formação por alternância - RC.               |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | decimal(8,2)                | Itinerário técnico/profissional com formação por alternância - RC.          |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | decimal(8,2)                | Educação profissional concomitante com formação por alternância - RC.       |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | decimal(8,2)                | Ens. Médio integrado profissional em instituições específicas - RC.         |
| `eja_integrada_profissional_rc_instituicoes_prof`          | decimal(8,2)                | EJA integrada profissional em instituições específicas - RC.                |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | decimal(8,2)                | Itinerário técnico/profissional em instituições específicas - RC.           |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | decimal(8,2)                | Educação profissional concomitante em instituições específicas - RC.        |
| `matriculas_totais`                                        | decimal(12,2)               | Total de matrículas consideradas nos cálculos de repasse.                   |
| `coeficiente_vaaf`                                         | decimal(20,12)              | Coeficiente de ponderação VAAT/VAAR (VAAF) para distribuição de recursos.   |
| `estimativa_receita_vaaf`                                  | decimal(18,2)               | Estimativa da receita total a receber via complementação da União.          |
| `municipality_id`                                          | bigint, FK                  | Identificador do município (chave estrangeira para a tabela de municípios). |

### Índices
- Index em (`id`,`creche_integral_rp`,`creche_parcial_rp`,`pre_escola_integral_rp`,`pre_escola_parcial_rp`,`ens_fund_iniciais_urbano_rp`,`ens_fund_iniciais_rural_rp`,`ens_fund_finais_urbano_rp`,`ens_fund_finais_rural_rp`,`ens_fund_integral_rp`,`ens_medio_urbano_rp`,`ens_medio_rural_rp`,`ens_medio_integral_rp`,`ens_medio_integrado_prof_rp`,`itinerario_formacao_tecnica_prof_rp`,`educacao_prof_concomitante_rp`,`educacao_especial_rp`,`aee`,`eja_avaliacao_processo_rp`,`eja_integrada_profissional_rp`,`educacao_indigena_quilombola_rp`,`creche_integral_rc`,`creche_parcial_rc`,`pre_escola_integral_rc`,`pre_escola_parcial_rc`,`educacao_especial_rc`,`ens_fund_finais_rural_rc_formacao_alternancia`,`ens_medio_rural_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_formacao_alternancia`,`educacao_indigena_quilombola_rc_formacao_alternancia`,`eja_avaliacao_processo_rc_formacao_alternancia`,`eja_integrada_profissional_rc_formacao_alternancia`,`itinerario_formacao_tecnica_prof_rc_formacao_alternancia`,`educacao_prof_concomitante_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_instituicoes_prof`,`eja_integrada_profissional_rc_instituicoes_prof`,`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,`educacao_prof_concomitante_rc_instituicoes_prof`,`matriculas_totais`,`coeficiente_vaaf`,`estimativa_receita_vaaf`,`municipality_id`) conforme definido em `Meta.indexes`.