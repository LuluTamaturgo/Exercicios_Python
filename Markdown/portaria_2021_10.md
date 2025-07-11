🗂️ Descrição Geral da Tabela portaria_2021_10
A tabela portaria_2021_10 armazena os valores de repasse por aluno (em R$) para o ano de 2021, com base na Portaria nº 10 do Fundeb. Os repasses consideram:

Etapas e modalidades de ensino (educação infantil, fundamental e média);

Localização (zona urbana ou rural);

Regime de ensino (tempo parcial ou integral);

Tipos de complementações: RC (Redistribuição Complementar), formação por alternância e instituições profissionais.

Essas informações são usadas para o cálculo da redistribuição dos recursos do Fundeb para os municípios brasileiros.

📄 Descrição dos Campos
| Campo                                                      | Tipo             | Obrigatório | Descrição                                                          |
| ---------------------------------------------------------- | ---------------- | ----------- | ------------------------------------------------------------------ |
| `id`                                                       | `bigint`         | Sim (PK)    | Identificador único da linha da tabela.                            |
| `creche_integral_rp`                                       | `decimal(8,2)`   | Não         | Valor por aluno da creche integral – repasse próprio (RP).         |
| `creche_parcial_rp`                                        | `decimal(8,2)`   | Não         | Valor por aluno da creche parcial – repasse próprio.               |
| `pre_escola_integral_rp`                                   | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola integral – repasse próprio.          |
| `pre_escola_parcial_rp`                                    | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola parcial – repasse próprio.           |
| `ens_fund_iniciais_urbano_rp`                              | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona urbana – repasse próprio. |
| `ens_fund_iniciais_rural_rp`                               | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona rural – repasse próprio.  |
| `ens_fund_finais_urbano_rp`                                | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona urbana – repasse próprio.   |
| `ens_fund_finais_rural_rp`                                 | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona rural – repasse próprio.    |
| `ens_fund_integral_rp`                                     | `decimal(8,2)`   | Não         | Ensino fundamental em tempo integral – repasse próprio.            |
| `ens_medio_urbano_rp`                                      | `decimal(8,2)`   | Não         | Ensino médio urbano – repasse próprio.                             |
| `ens_medio_rural_rp`                                       | `decimal(8,2)`   | Não         | Ensino médio rural – repasse próprio.                              |
| `ens_medio_integral_rp`                                    | `decimal(8,2)`   | Não         | Ensino médio em tempo integral – repasse próprio.                  |
| `ens_medio_integrado_prof_rp`                              | `decimal(8,2)`   | Não         | Médio integrado à formação profissional – repasse próprio.         |
| `itinerario_formacao_tecnica_prof_rp`                      | `decimal(8,2)`   | Não         | Itinerário técnico/profissional – repasse próprio.                 |
| `educacao_prof_concomitante_rp`                            | `decimal(8,2)`   | Não         | Educação profissional concomitante – repasse próprio.              |
| `educacao_especial_rp`                                     | `decimal(8,2)`   | Não         | Educação especial – repasse próprio.                               |
| `aee`                                                      | `decimal(8,2)`   | Não         | Atendimento educacional especializado – repasse próprio.           |
| `eja_avaliacao_processo_rp`                                | `decimal(8,2)`   | Não         | EJA com avaliação por processo – repasse próprio.                  |
| `eja_integrada_profissional_rp`                            | `decimal(8,2)`   | Não         | EJA integrada à formação profissional – repasse próprio.           |
| `educacao_indigena_quilombola_rp`                          | `decimal(8,2)`   | Não         | Educação indígena e quilombola – repasse próprio.                  |
| `creche_integral_rc`                                       | `decimal(8,2)`   | Não         | Complementação RC – creche integral.                               |
| `creche_parcial_rc`                                        | `decimal(8,2)`   | Não         | Complementação RC – creche parcial.                                |
| `pre_escola_integral_rc`                                   | `decimal(8,2)`   | Não         | Complementação RC – pré-escola integral.                           |
| `pre_escola_parcial_rc`                                    | `decimal(8,2)`   | Não         | Complementação RC – pré-escola parcial.                            |
| `educacao_especial_rc`                                     | `decimal(8,2)`   | Não         | Complementação RC – educação especial.                             |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | `decimal(8,2)`   | Não         | Fund. finais – rural com formação por alternância – RC.            |
| `ens_medio_rural_rc_formacao_alternancia`                  | `decimal(8,2)`   | Não         | Ensino médio rural com formação por alternância – RC.              |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | `decimal(8,2)`   | Não         | Médio integrado profissional com alternância – RC.                 |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | `decimal(8,2)`   | Não         | Educação indígena/quilombola com alternância – RC.                 |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | `decimal(8,2)`   | Não         | EJA com avaliação por processo com alternância – RC.               |
| `eja_integrada_profissional_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | EJA integrada profissional com alternância – RC.                   |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | `decimal(8,2)`   | Não         | Itinerário técnico/profissional com alternância – RC.              |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | Educação prof. concomitante com alternância – RC.                  |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | `decimal(8,2)`   | Não         | Médio integrado – instituições profissionais – RC.                 |
| `eja_integrada_profissional_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | EJA profissional – instituições profissionais – RC.                |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | `decimal(8,2)`   | Não         | Itinerário técnico – instituições profissionais – RC.              |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | Educação prof. concomitante – instituições prof. – RC.             |
| `matriculas_totais`                                        | `decimal(12,2)`  | Não         | Total de matrículas consideradas no Fundeb.                        |
| `coeficiente_vaaf`                                         | `decimal(20,12)` | Não         | Coeficiente do Valor Aluno/Ano Fundeb (VAAF).                      |
| `estimativa_receita_vaaf`                                  | `decimal(18,2)`  | Não         | Estimativa de receita total do município com base no VAAF.         |
| `municipality_id`                                          | `bigint`         | Sim (FK)    | Referência ao município associado a este repasse.                  |


### Índices
- Index em (``, 


`id`,
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
`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,`,
`educacao_prof_concomitante_rc_instituicoes_prof`,
`matriculas_totais`,
`coeficiente_vaaf`,
`estimativa_receita_vaaf`,
`municipality_id`) conforme definido em `Meta.indexes`.