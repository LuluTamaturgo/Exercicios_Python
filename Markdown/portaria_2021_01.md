🗂️ Descrição Geral da Tabela portaria_2021_01
A tabela portaria_2021_01 armazena os valores de repasse por aluno (em R$) no ano de 2021, considerando diferentes etapas e modalidades de ensino, zonas urbana e rural, tempo integral/parcial, bem como tipos de complementações (como formação por alternância ou instituições profissionais).
Esses valores são utilizados no cálculo da redistribuição dos recursos do Fundeb entre os municípios brasileiros

📄 Descrição dos Campos
| Campo             | Tipo     | Obrigatório               | Descrição                                                         |
| ----------------- | -------- | ------------------------- | ----------------------------------------------------------------- |
| `id`              | `bigint` | Sim (PK, auto\_increment) | Identificador único da linha na tabela.                           |
| `municipality_id` | `bigint` | Sim (FK)                  | Chave estrangeira para o município ao qual os valores se referem. |

▶️ Repasse Próprio (RP)
| Campo                                 | Tipo           | Descrição                                                          |
| ------------------------------------- | -------------- | ------------------------------------------------------------------ |
| `creche_integral_rp`                  | `decimal(8,2)` | Valor por aluno na creche em tempo integral – repasse próprio.     |
| `creche_parcial_rp`                   | `decimal(8,2)` | Valor por aluno na creche em tempo parcial – repasse próprio.      |
| `pre_escola_integral_rp`              | `decimal(8,2)` | Valor por aluno na pré-escola em tempo integral – repasse próprio. |
| `pre_escola_parcial_rp`               | `decimal(8,2)` | Valor por aluno na pré-escola em tempo parcial – repasse próprio.  |
| `ens_fund_iniciais_urbano_rp`         | `decimal(8,2)` | Ensino fundamental (anos iniciais), zona urbana – repasse próprio. |
| `ens_fund_iniciais_rural_rp`          | `decimal(8,2)` | Ensino fundamental (anos iniciais), zona rural – repasse próprio.  |
| `ens_fund_finais_urbano_rp`           | `decimal(8,2)` | Ensino fundamental (anos finais), zona urbana – repasse próprio.   |
| `ens_fund_finais_rural_rp`            | `decimal(8,2)` | Ensino fundamental (anos finais), zona rural – repasse próprio.    |
| `ens_fund_integral_rp`                | `decimal(8,2)` | Ensino fundamental em tempo integral – repasse próprio.            |
| `ens_medio_urbano_rp`                 | `decimal(8,2)` | Ensino médio, zona urbana – repasse próprio.                       |
| `ens_medio_rural_rp`                  | `decimal(8,2)` | Ensino médio, zona rural – repasse próprio.                        |
| `ens_medio_integral_rp`               | `decimal(8,2)` | Ensino médio em tempo integral – repasse próprio.                  |
| `ens_medio_integrado_prof_rp`         | `decimal(8,2)` | Médio integrado à formação profissional – repasse próprio.         |
| `itinerario_formacao_tecnica_prof_rp` | `decimal(8,2)` | Itinerário de formação técnica/profissional – repasse próprio.     |
| `educacao_prof_concomitante_rp`       | `decimal(8,2)` | Educação profissional concomitante – repasse próprio.              |
| `educacao_especial_rp`                | `decimal(8,2)` | Educação especial – repasse próprio.                               |
| `aee`                                 | `decimal(8,2)` | Atendimento educacional especializado – repasse próprio.           |
| `eja_avaliacao_processo_rp`           | `decimal(8,2)` | Educação de Jovens e Adultos com avaliação por processo – RP.      |
| `eja_integrada_profissional_rp`       | `decimal(8,2)` | EJA integrada à formação profissional – repasse próprio.           |
| `educacao_indigena_quilombola_rp`     | `decimal(8,2)` | Educação indígena e quilombola – repasse próprio.                  |


🧩 Complementação RC
| Campo                    | Tipo           | Descrição                                   |
| ------------------------ | -------------- | ------------------------------------------- |
| `creche_integral_rc`     | `decimal(8,2)` | Complementação RC para creche integral.     |
| `creche_parcial_rc`      | `decimal(8,2)` | Complementação RC para creche parcial.      |
| `pre_escola_integral_rc` | `decimal(8,2)` | Complementação RC para pré-escola integral. |
| `pre_escola_parcial_rc`  | `decimal(8,2)` | Complementação RC para pré-escola parcial.  |
| `educacao_especial_rc`   | `decimal(8,2)` | Complementação RC para educação especial.   |


🧭 Formação por Alternância (RC)
| Campo                                                      | Tipo           | Descrição                                                  |
| ---------------------------------------------------------- | -------------- | ---------------------------------------------------------- |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | `decimal(8,2)` | Fund. anos finais – rural, com formação por alternância.   |
| `ens_medio_rural_rc_formacao_alternancia`                  | `decimal(8,2)` | Ensino médio rural com formação por alternância.           |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | `decimal(8,2)` | Médio integrado profissional com formação por alternância. |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | `decimal(8,2)` | Educação indígena/quilombola com alternância.              |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | `decimal(8,2)` | EJA com avaliação por processo com alternância.            |
| `eja_integrada_profissional_rc_formacao_alternancia`       | `decimal(8,2)` | EJA integrada profissional com alternância.                |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | `decimal(8,2)` | Itinerário técnico/profissional com alternância.           |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | `decimal(8,2)` | Educação profissional concomitante com alternância.        |

🏫 Instituições Profissionais (RC)
| Campo                                                   | Tipo           | Descrição                                                        |
| ------------------------------------------------------- | -------------- | ---------------------------------------------------------------- |
| `ens_medio_integrado_prof_rc_instituicoes_prof`         | `decimal(8,2)` | Médio integrado – instituições profissionais.                    |
| `eja_integrada_profissional_rc_instituicoes_prof`       | `decimal(8,2)` | EJA profissional – instituições profissionais.                   |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof` | `decimal(8,2)` | Itinerário técnico – instituições profissionais.                 |
| `educacao_prof_concomitante_rc_instituicoes_prof`       | `decimal(8,2)` | Educação profissional concomitante – instituições profissionais. |


📊 Consolidação
| Campo                     | Tipo             | Descrição                                                  |
| ------------------------- | ---------------- | ---------------------------------------------------------- |
| `matriculas_totais`       | `decimal(12,2)`  | Total de matrículas consideradas no cálculo do Fundeb.     |
| `coeficiente_vaaf`        | `decimal(20,12)` | Coeficiente do Valor Aluno Ano Fundeb (VAAF).              |
| `estimativa_receita_vaaf` | `decimal(18,2)`  | Estimativa de receita total do município com base no VAAF. |


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
`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,
`educacao_prof_concomitante_rc_instituicoes_prof`,
`matriculas_totais`,
`coeficiente_vaaf`,
`estimativa_receita_vaaf`,
`municipality_id`) conforme definido em `Meta.indexes`.