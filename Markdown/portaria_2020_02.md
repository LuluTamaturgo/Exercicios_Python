A tabela portaria_2020_02 armazena informações detalhadas sobre repasses financeiros e indicadores educacionais relacionados ao financiamento da educação básica, provavelmente com base nos critérios da Portaria Interministerial nº 2/2020, que trata da distribuição dos recursos do FUNDEB no Brasil. A tabela separa os valores de repasse por modalidade, etapa e regime de ensino, com variações conforme a complementação da União: VAAR e VAAF (nesse caso, foca em VAAF).

📊 Descrição Geral da Tabela portaria_2020_02
Finalidade: Armazenar os valores de repasse por aluno (em R$) e outros dados relevantes para o cálculo da redistribuição dos recursos do Fundeb em 2020.

Chave primária: id

Relacionamento: Campo municipality_id provavelmente se relaciona com uma tabela de municípios (ex: municipality), o que indica que cada linha se refere a um município específico.

🧩 Descrição de cada campo

| Campo                                       | Tipo           | Descrição                                                             |
| ------------------------------------------- | -------------- | --------------------------------------------------------------------- |
| **id**                                      | `bigint`       | Identificador único da linha (auto incremento).                       |
| **creche\_integral\_rp**                    | `decimal(8,2)` | Valor por aluno da creche em tempo integral – repasse próprio (`rp`). |
| **creche\_parcial\_rp**                     | `decimal(8,2)` | Valor por aluno da creche em tempo parcial – repasse próprio.         |
| **pre\_escola\_integral\_rp**               | `decimal(8,2)` | Valor por aluno da pré-escola em tempo integral – repasse próprio.    |
| **pre\_escola\_parcial\_rp**                | `decimal(8,2)` | Valor por aluno da pré-escola parcial – repasse próprio.              |
| **ens\_fund\_iniciais\_urbano\_rp**         | `decimal(8,2)` | Ensino fundamental – anos iniciais, zona urbana – repasse próprio.    |
| **ens\_fund\_iniciais\_rural\_rp**          | `decimal(8,2)` | Ensino fundamental – anos iniciais, zona rural – repasse próprio.     |
| **ens\_fund\_finais\_urbano\_rp**           | `decimal(8,2)` | Ensino fundamental – anos finais, zona urbana – repasse próprio.      |
| **ens\_fund\_finais\_rural\_rp**            | `decimal(8,2)` | Ensino fundamental – anos finais, zona rural – repasse próprio.       |
| **ens\_fund\_integral\_rp**                 | `decimal(8,2)` | Ensino fundamental – tempo integral – repasse próprio.                |
| **ens\_medio\_urbano\_rp**                  | `decimal(8,2)` | Ensino médio – urbano – repasse próprio.                              |
| **ens\_medio\_rural\_rp**                   | `decimal(8,2)` | Ensino médio – rural – repasse próprio.                               |
| **ens\_medio\_integral\_rp**                | `decimal(8,2)` | Ensino médio – tempo integral – repasse próprio.                      |
| **ens\_medio\_integrado\_prof\_rp**         | `decimal(8,2)` | Ensino médio integrado à educação profissional – repasse próprio.     |
| **itinerario\_formacao\_tecnica\_prof\_rp** | `decimal(8,2)` | Itinerário de formação técnica e profissional – repasse próprio.      |
| **educacao\_prof\_concomitante\_rp**        | `decimal(8,2)` | Educação profissional de forma concomitante – repasse próprio.        |
| **educacao\_especial\_rp**                  | `decimal(8,2)` | Educação especial (ex: alunos com deficiência) – repasse próprio.     |
| **aee**                                     | `decimal(8,2)` | Atendimento educacional especializado – repasse próprio.              |
| **eja\_avaliacao\_processo\_rp**            | `decimal(8,2)` | EJA com avaliação por processo – repasse próprio.                     |
| **eja\_integrada\_profissional\_rp**        | `decimal(8,2)` | EJA integrada à educação profissional – repasse próprio.              |
| **educacao\_indigena\_quilombola\_rp**      | `decimal(8,2)` | Educação indígena e quilombola – repasse próprio.                     |

🔄 Campos com sufixo _rc

Refere-se a "repasse com complementação" da União – no caso, ainda parte do VAAF (Valor Anual por Aluno Fundeb).
| Campo                                                              | Tipo           | Descrição                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **creche\_integral\_rc**                                           | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **creche\_parcial\_rc**                                            | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **pre\_escola_integral\_rc**                                       | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **pre\_escola\_parcial\_rc**                                       | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **educacao\_especial\_rc**                                         | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **ens\_fund\_finais\_rural\_rc\_formacao\_alternancia**            | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **ens\_medio\_rural\_rc\_formacao\_alternancia**                   | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **ens\_medio\_integrado\_prof\_rc\_formacao\_alternancia**         | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **educacao\_indigena\_quilombola\_rc\_formacao\_alternancia**      | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **eja\_avaliacao\_processo\_rc\_formacao\_alternancia**            | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **eja\_integrada\_profissional\_rc\_formacao\_alternancia**        | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **itinerario\_formacao\_tecnica\_prof\_rc\_formacao\_alternancia** | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **educacao\_prof\_concomitante\_rc\_formacao\_alternancia**        | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **ens\_medio\_integrado\_prof\_rc\_instituicoes\_prof**            | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **eja\_integrada\_profissional\_rc\_instituicoes\_prof**           | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **itinerario\_formacao\_tecnica\_prof\_rc\_instituicoes\_prof**    | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |
| **educacao\_prof\_concomitante\_rc\_instituicoes\_prof**           | `decimal(8,2)` | Representam os valores de repasse para cada modalidade com complementações específicas, como:formação por alternância: alternância entre escola e comunidade, comum em áreas rurais; instituições profissionais: como institutos federais e escolas técnicas.                    |

🧮 Campos agregadores e indicadores
| Campo                         | Tipo             | Descrição                                                      |
| ----------------------------- | ---------------- | -------------------------------------------------------------- |
| **matriculas\_totais**        | `decimal(12,2)`  | Total de matrículas consideradas no cálculo.                   |
| **coeficiente\_vaaf**         | `decimal(20,12)` | Coeficiente do Valor Aluno Ano Fundeb (VAAF) para o município. |
| **estimativa\_receita\_vaaf** | `decimal(18,2)`  | Estimativa de receita total do município com base no VAAF.     |

🌎 Relacionamento com municípios
| Campo                | Tipo     | Descrição                                                                         |
| -------------------- | -------- | --------------------------------------------------------------------------------- |
| **municipality\_id** | `bigint` | Chave estrangeira que identifica o município ao qual os dados da linha pertencem. |


### Índices
- Index em (`id`,`creche_integral_rp`,`creche_parcial_rp`,`pre_escola_integral_rp`,`pre_escola_parcial_rp`,`ens_fund_iniciais_urbano_rp`,`ens_fund_iniciais_rural_rp`,`ens_fund_finais_urbano_rp`,`ens_fund_finais_rural_rp`,`ens_fund_integral_rp`,`ens_medio_urbano_rp`,`ens_medio_rural_rp`,`ens_medio_integral_rp`,`ens_medio_integrado_prof_rp`,`itinerario_formacao_tecnica_prof_rp`,`educacao_prof_concomitante_rp`,`educacao_especial_rp`,`aee`,`eja_avaliacao_processo_rp`,`eja_integrada_profissional_rp`,`educacao_indigena_quilombola_rp`,`creche_integral_rc`,`creche_parcial_rc`,`pre_escola_integral_rc`,`pre_escola_parcial_rc`,`educacao_especial_rc`,`ens_fund_finais_rural_rc_formacao_alternancia`,`ens_medio_rural_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_formacao_alternancia`,`educacao_indigena_quilombola_rc_formacao_alternancia`,`eja_avaliacao_processo_rc_formacao_alternancia`,`eja_integrada_profissional_rc_formacao_alternancia`,`itinerario_formacao_tecnica_prof_rc_formacao_alternancia`,`educacao_prof_concomitante_rc_formacao_alternancia`,`ens_medio_integrado_prof_rc_instituicoes_prof`,`eja_integrada_profissional_rc_instituicoes_prof`,`itinerario_formacao_tecnica_prof_rc_instituicoes_prof`,`educacao_prof_concomitante_rc_instituicoes_prof`,`matriculas_totais`,`coeficiente_vaaf`,`estimativa_receita_vaaf`,`municipality_id`) conforme definido em `Meta.indexes`.