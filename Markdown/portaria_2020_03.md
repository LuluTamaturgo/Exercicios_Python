🗂️ Descrição Geral da Tabela portaria_2020_03
A tabela portaria_2020_03 armazena os valores de repasse por aluno (em R$) em 2020, conforme as modalidades de ensino, turnos, áreas (urbana/rural), e tipos de complementações (como formação por alternância ou instituições profissionais). Esses valores são utilizados para o cálculo da redistribuição dos recursos do Fundeb para os municípios.

Essa tabela tem papel estratégico na estimativa da receita do município via o VAAF (Valor Anual por Aluno Fundeb) e no cálculo do coeficiente de redistribuição dos recursos.

🧱 Descrição dos Campos
| Campo                | Tipo     | Descrição                                                         |
| -------------------- | -------- | ----------------------------------------------------------------- |
| **id**               | `bigint` | Identificador único da linha. Chave primária com auto incremento. |
| **municipality\_id** | `bigint` | Chave estrangeira que liga os dados ao respectivo município.      |

👶 Educação Infantil
| Campo                         | Tipo           | Descrição                                                           |
| ----------------------------- | -------------- | ------------------------------------------------------------------- |
| **creche\_integral\_rp**      | `decimal(8,2)` | Valor por aluno da creche em tempo integral – repasse próprio (RP). |
| **creche\_parcial\_rp**       | `decimal(8,2)` | Valor por aluno da creche em tempo parcial – repasse próprio.       |
| **pre\_escola\_integral\_rp** | `decimal(8,2)` | Valor por aluno da pré-escola em tempo integral – repasse próprio.  |
| **pre\_escola\_parcial\_rp**  | `decimal(8,2)` | Valor por aluno da pré-escola parcial – repasse próprio.            |

📚 Ensino Fundamental
| Campo                               | Tipo           | Descrição                                               |
| ----------------------------------- | -------------- | ------------------------------------------------------- |
| **ens\_fund\_iniciais\_urbano\_rp** | `decimal(8,2)` | Anos iniciais, zona urbana – repasse próprio.           |
| **ens\_fund\_iniciais\_rural\_rp**  | `decimal(8,2)` | Anos iniciais, zona rural – repasse próprio.            |
| **ens\_fund\_finais\_urbano\_rp**   | `decimal(8,2)` | Anos finais, zona urbana – repasse próprio.             |
| **ens\_fund\_finais\_rural\_rp**    | `decimal(8,2)` | Anos finais, zona rural – repasse próprio.              |
| **ens\_fund\_integral\_rp**         | `decimal(8,2)` | Ensino fundamental em tempo integral – repasse próprio. |

🎓 Ensino Médio
| Campo                               | Tipo           | Descrição                                                  |
| ----------------------------------- | -------------- | ---------------------------------------------------------- |
| **ens\_medio\_urbano\_rp**          | `decimal(8,2)` | Ensino médio, urbano – repasse próprio.                    |
| **ens\_medio\_rural\_rp**           | `decimal(8,2)` | Ensino médio, rural – repasse próprio.                     |
| **ens\_medio\_integral\_rp**        | `decimal(8,2)` | Ensino médio em tempo integral – repasse próprio.          |
| **ens\_medio\_integrado\_prof\_rp** | `decimal(8,2)` | Médio integrado à educação profissional – repasse próprio. |

🛠️ Educação Profissional e Técnica
| Campo                                       | Tipo           | Descrição                                                                |
| ------------------------------------------- | -------------- | ------------------------------------------------------------------------ |
| **itinerario\_formacao\_tecnica\_prof\_rp** | `decimal(8,2)` | Itinerário de formação técnica e profissional – repasse próprio.         |
| **educacao\_prof\_concomitante\_rp**        | `decimal(8,2)` | Educação profissional oferecida de forma concomitante – repasse próprio. |

👥 Inclusão e Diversidade
| Campo                                  | Tipo           | Descrição                                                     |
| -------------------------------------- | -------------- | ------------------------------------------------------------- |
| **educacao\_especial\_rp**             | `decimal(8,2)` | Educação especial (alunos com deficiência) – repasse próprio. |
| **aee**                                | `decimal(8,2)` | Atendimento educacional especializado – repasse próprio.      |
| **educacao\_indigena\_quilombola\_rp** | `decimal(8,2)` | Educação indígena e quilombola – repasse próprio.             |


📘 Educação de Jovens e Adultos (EJA)
| Campo                                | Tipo           | Descrição                                                |
| ------------------------------------ | -------------- | -------------------------------------------------------- |
| **eja\_avaliacao\_processo\_rp**     | `decimal(8,2)` | EJA com avaliação por processo – repasse próprio.        |
| **eja\_integrada\_profissional\_rp** | `decimal(8,2)` | EJA integrada à educação profissional – repasse próprio. |

🏫 Complementações Específicas (RC)
Valores com complementações diferenciadas:

Formação por alternância: alterna períodos entre escola e comunidade (ex: agroecologia, educação do campo).

Instituições profissionais: institutos federais, escolas técnicas etc.
| Campo                                                                                                                                      | Tipo           | Descrição                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------- |
| **creche\_integral\_rc**, **creche\_parcial\_rc**, **pre\_escola\_integral\_rc**, **pre\_escola\_parcial\_rc**, **educacao\_especial\_rc** | `decimal(8,2)` | Repasses para educação infantil e especial com complementação RC. |
| **ens\_fund\_finais\_rural\_rc\_formacao\_alternancia**, **ens\_medio\_rural\_rc\_formacao\_alternancia**, **ens\_medio\_integrado\_prof\_rc\_formacao\_alternancia**, **educacao\_indigena\_quilombola\_rc\_formacao\_alternancia**, **eja\_avaliacao\_processo\_rc\_formacao\_alternancia**, **eja\_integrada\_profissional\_rc\_formacao\_alternancia**, **itinerario\_formacao\_tecnica\_prof\_rc\_formacao\_alternancia**, **educacao\_prof\_concomitante\_rc\_formacao\_alternancia** | `decimal(8,2)` | Repasses para educação infantil e especial com complementação RC. |
| **ens\_medio\_integrado\_prof\_rc\_instituicoes\_prof**, **eja\_integrada\_profissional\_rc\_instituicoes\_prof**, **itinerario\_formacao\_tecnica\_prof\_rc\_instituicoes\_prof**, **educacao\_prof\_concomitante\_rc\_instituicoes\_prof ** | `decimal(8,2)` | Repasses para instituições profissionais. |

📈 Totais e Cálculo do VAAF
| Campo                         | Tipo             | Descrição                                                               |
| ----------------------------- | ---------------- | ----------------------------------------------------------------------- |
| **matriculas\_totais**        | `decimal(12,2)`  | Total de matrículas consideradas no cálculo para o município.           |
| **coeficiente\_vaaf**         | `decimal(20,12)` | Coeficiente do Valor Aluno Ano Fundeb para redistribuição dos recursos. |
| **estimativa\_receita\_vaaf** | `decimal(18,2)`  | Estimativa da receita total do município com base no coeficiente VAAF.  |

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