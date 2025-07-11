🗂️ Descrição Geral da Tabela portaria_2022_02
A tabela portaria_2022_02 armazena os valores de repasse por aluno (em R$) referentes ao ano de 2022, definidos por uma segunda portaria normativa do Fundeb. Os valores consideram:

Etapas e modalidades da educação (infantil, fundamental, média, EJA, especial, profissionalizante);

Localização da escola (zona urbana ou rural);

Regime de ensino (tempo parcial ou integral);

Tipos específicos de complementações:

RP (Repasse Próprio),

RC (Redistribuição Complementar),

Formação por alternância,

Instituições profissionais.

Essa tabela é usada como referência para o cálculo do Valor Aluno Ano (VAAF) e da estimativa de receita para cada município, garantindo uma distribuição mais equitativa dos recursos do Fundeb.

| Campo                                                      | Tipo             | Obrigatório | Descrição                                                      |
| ---------------------------------------------------------- | ---------------- | ----------- | -------------------------------------------------------------- |
| `id`                                                       | `bigint`         | Sim (PK)    | Identificador único da linha da tabela.                        |
| `creche_integral_rp`                                       | `decimal(8,2)`   | Não         | Valor por aluno na creche integral – repasse próprio (RP).     |
| `creche_parcial_rp`                                        | `decimal(8,2)`   | Não         | Valor por aluno na creche parcial – repasse próprio.           |
| `pre_escola_integral_rp`                                   | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola integral – repasse próprio.      |
| `pre_escola_parcial_rp`                                    | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola parcial – repasse próprio.       |
| `ens_fund_iniciais_urbano_rp`                              | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona urbana – RP.          |
| `ens_fund_iniciais_rural_rp`                               | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona rural – RP.           |
| `ens_fund_finais_urbano_rp`                                | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona urbana – RP.            |
| `ens_fund_finais_rural_rp`                                 | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona rural – RP.             |
| `ens_fund_integral_rp`                                     | `decimal(8,2)`   | Não         | Ensino fundamental em tempo integral – RP.                     |
| `ens_medio_urbano_rp`                                      | `decimal(8,2)`   | Não         | Ensino médio urbano – repasse próprio.                         |
| `ens_medio_rural_rp`                                       | `decimal(8,2)`   | Não         | Ensino médio rural – repasse próprio.                          |
| `ens_medio_integral_rp`                                    | `decimal(8,2)`   | Não         | Ensino médio integral – repasse próprio.                       |
| `ens_medio_integrado_prof_rp`                              | `decimal(8,2)`   | Não         | Ensino médio integrado à formação profissional – RP.           |
| `itinerario_formacao_tecnica_prof_rp`                      | `decimal(8,2)`   | Não         | Itinerário técnico-profissional – RP.                          |
| `educacao_prof_concomitante_rp`                            | `decimal(8,2)`   | Não         | Educação profissional concomitante – RP.                       |
| `educacao_especial_rp`                                     | `decimal(8,2)`   | Não         | Educação especial – repasse próprio.                           |
| `aee`                                                      | `decimal(8,2)`   | Não         | Atendimento Educacional Especializado – repasse próprio.       |
| `eja_avaliacao_processo_rp`                                | `decimal(8,2)`   | Não         | EJA com avaliação por processo – repasse próprio.              |
| `eja_integrada_profissional_rp`                            | `decimal(8,2)`   | Não         | EJA integrada à formação profissional – RP.                    |
| `educacao_indigena_quilombola_rp`                          | `decimal(8,2)`   | Não         | Educação indígena e quilombola – RP.                           |
| `creche_integral_rc`                                       | `decimal(8,2)`   | Não         | Complementação RC para creche integral.                        |
| `creche_parcial_rc`                                        | `decimal(8,2)`   | Não         | Complementação RC para creche parcial.                         |
| `pre_escola_integral_rc`                                   | `decimal(8,2)`   | Não         | Complementação RC para pré-escola integral.                    |
| `pre_escola_parcial_rc`                                    | `decimal(8,2)`   | Não         | Complementação RC para pré-escola parcial.                     |
| `educacao_especial_rc`                                     | `decimal(8,2)`   | Não         | Complementação RC para educação especial.                      |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | `decimal(8,2)`   | Não         | Ensino fund. final rural com formação por alternância – RC.    |
| `ens_medio_rural_rc_formacao_alternancia`                  | `decimal(8,2)`   | Não         | Ensino médio rural com formação por alternância – RC.          |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | `decimal(8,2)`   | Não         | Médio integrado profissional com alternância – RC.             |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | `decimal(8,2)`   | Não         | Educação indígena/quilombola com alternância – RC.             |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | `decimal(8,2)`   | Não         | EJA com avaliação por processo com alternância – RC.           |
| `eja_integrada_profissional_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | EJA integrada profissional com alternância – RC.               |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | `decimal(8,2)`   | Não         | Itinerário técnico/profissional com alternância – RC.          |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | Educação prof. concomitante com alternância – RC.              |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | `decimal(8,2)`   | Não         | Médio integrado – instituições profissionais – RC.             |
| `eja_integrada_profissional_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | EJA profissional – instituições profissionais – RC.            |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | `decimal(8,2)`   | Não         | Itinerário técnico – instituições profissionais – RC.          |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | Educação prof. concomitante – instituições profissionais – RC. |
| `matriculas_totais`                                        | `decimal(12,2)`  | Não         | Total de matrículas consideradas no Fundeb.                    |
| `coeficiente_vaaf`                                         | `decimal(20,12)` | Não         | Coeficiente do Valor Aluno/Ano Fundeb (VAAF).                  |
| `estimativa_receita_vaaf`                                  | `decimal(18,2)`  | Não         | Estimativa da receita total do município com base no VAAF.     |
| `municipality_id`                                          | `bigint`         | Sim (FK)    | Chave estrangeira que referencia o município correspondente.   |


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