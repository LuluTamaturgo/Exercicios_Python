🗂️ Descrição Geral da Tabela portaria_2021_03
A tabela portaria_2021_03 armazena os valores de repasse por aluno (em R$) para o ano de 2021, conforme definidos em uma terceira portaria complementar do Fundeb. Ela considera diversas etapas e modalidades de ensino, zonas urbana e rural, tempo integral ou parcial, além de tipos específicos de complementações (como por formação por alternância e instituições profissionais). Esses dados são usados para calcular o valor a ser redistribuído entre os municípios brasileiros no âmbito do Fundeb.

📄 Descrição dos Campos
| Campo                                                      | Tipo             | Obrigatório | Descrição                                                                 |
| ---------------------------------------------------------- | ---------------- | ----------- | ------------------------------------------------------------------------- |
| `id`                                                       | `bigint`         | Sim (PK)    | Identificador único da linha da tabela.                                   |
| `creche_integral_rp`                                       | `decimal(8,2)`   | Não         | Valor por aluno na creche em tempo integral – repasse próprio.            |
| `creche_parcial_rp`                                        | `decimal(8,2)`   | Não         | Valor por aluno na creche em tempo parcial – repasse próprio.             |
| `pre_escola_integral_rp`                                   | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola em tempo integral – repasse próprio.        |
| `pre_escola_parcial_rp`                                    | `decimal(8,2)`   | Não         | Valor por aluno na pré-escola em tempo parcial – repasse próprio.         |
| `ens_fund_iniciais_urbano_rp`                              | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona urbana – repasse próprio.        |
| `ens_fund_iniciais_rural_rp`                               | `decimal(8,2)`   | Não         | Ensino fundamental (anos iniciais), zona rural – repasse próprio.         |
| `ens_fund_finais_urbano_rp`                                | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona urbana – repasse próprio.          |
| `ens_fund_finais_rural_rp`                                 | `decimal(8,2)`   | Não         | Ensino fundamental (anos finais), zona rural – repasse próprio.           |
| `ens_fund_integral_rp`                                     | `decimal(8,2)`   | Não         | Ensino fundamental em tempo integral – repasse próprio.                   |
| `ens_medio_urbano_rp`                                      | `decimal(8,2)`   | Não         | Ensino médio, zona urbana – repasse próprio.                              |
| `ens_medio_rural_rp`                                       | `decimal(8,2)`   | Não         | Ensino médio, zona rural – repasse próprio.                               |
| `ens_medio_integral_rp`                                    | `decimal(8,2)`   | Não         | Ensino médio em tempo integral – repasse próprio.                         |
| `ens_medio_integrado_prof_rp`                              | `decimal(8,2)`   | Não         | Ensino médio integrado à formação profissional – repasse próprio.         |
| `itinerario_formacao_tecnica_prof_rp`                      | `decimal(8,2)`   | Não         | Itinerário de formação técnica e profissional – repasse próprio.          |
| `educacao_prof_concomitante_rp`                            | `decimal(8,2)`   | Não         | Educação profissional concomitante – repasse próprio.                     |
| `educacao_especial_rp`                                     | `decimal(8,2)`   | Não         | Educação especial – repasse próprio.                                      |
| `aee`                                                      | `decimal(8,2)`   | Não         | Atendimento educacional especializado (AEE) – repasse próprio.            |
| `eja_avaliacao_processo_rp`                                | `decimal(8,2)`   | Não         | EJA com avaliação por processo – repasse próprio.                         |
| `eja_integrada_profissional_rp`                            | `decimal(8,2)`   | Não         | EJA integrada à formação profissional – repasse próprio.                  |
| `educacao_indigena_quilombola_rp`                          | `decimal(8,2)`   | Não         | Educação indígena e quilombola – repasse próprio.                         |
| `creche_integral_rc`                                       | `decimal(8,2)`   | Não         | Complementação RC para creche em tempo integral.                          |
| `creche_parcial_rc`                                        | `decimal(8,2)`   | Não         | Complementação RC para creche em tempo parcial.                           |
| `pre_escola_integral_rc`                                   | `decimal(8,2)`   | Não         | Complementação RC para pré-escola integral.                               |
| `pre_escola_parcial_rc`                                    | `decimal(8,2)`   | Não         | Complementação RC para pré-escola parcial.                                |
| `educacao_especial_rc`                                     | `decimal(8,2)`   | Não         | Complementação RC para educação especial.                                 |
| `ens_fund_finais_rural_rc_formacao_alternancia`            | `decimal(8,2)`   | Não         | Ensino fund. final rural com formação por alternância – RC.               |
| `ens_medio_rural_rc_formacao_alternancia`                  | `decimal(8,2)`   | Não         | Ensino médio rural com formação por alternância – RC.                     |
| `ens_medio_integrado_prof_rc_formacao_alternancia`         | `decimal(8,2)`   | Não         | Médio integrado profissional com alternância – RC.                        |
| `educacao_indigena_quilombola_rc_formacao_alternancia`     | `decimal(8,2)`   | Não         | Educação indígena/quilombola com alternância – RC.                        |
| `eja_avaliacao_processo_rc_formacao_alternancia`           | `decimal(8,2)`   | Não         | EJA com avaliação por processo com alternância – RC.                      |
| `eja_integrada_profissional_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | EJA integrada profissional com alternância – RC.                          |
| `itinerario_formacao_tecnica_prof_rc_formacao_alternancia` | `decimal(8,2)`   | Não         | Itinerário técnico/profissional com alternância – RC.                     |
| `educacao_prof_concomitante_rc_formacao_alternancia`       | `decimal(8,2)`   | Não         | Educação profissional concomitante com alternância – RC.                  |
| `ens_medio_integrado_prof_rc_instituicoes_prof`            | `decimal(8,2)`   | Não         | Médio integrado – instituições profissionais – RC.                        |
| `eja_integrada_profissional_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | EJA profissional – instituições profissionais – RC.                       |
| `itinerario_formacao_tecnica_prof_rc_instituicoes_prof`    | `decimal(8,2)`   | Não         | Itinerário técnico – instituições profissionais – RC.                     |
| `educacao_prof_concomitante_rc_instituicoes_prof`          | `decimal(8,2)`   | Não         | Educação profissional concomitante – instituições prof. – RC.             |
| `matriculas_totais`                                        | `decimal(12,2)`  | Não         | Total de matrículas consideradas no cálculo do Fundeb.                    |
| `coeficiente_vaaf`                                         | `decimal(20,12)` | Não         | Coeficiente do Valor Aluno/Ano Fundeb (VAAF).                             |
| `estimativa_receita_vaaf`                                  | `decimal(18,2)`  | Não         | Estimativa da receita total para o município com base no VAAF.            |
| `municipality_id`                                          | `bigint`         | Sim (FK)    | Chave estrangeira que referencia o município a que os valores se referem. |


🔗 Relacionamentos
municipality_id: chave estrangeira para a tabela que armazena os municípios (geralmente uma tabela municipalities ou similar).

Os demais campos são valores monetários específicos, sem referência direta a outras tabelas.


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