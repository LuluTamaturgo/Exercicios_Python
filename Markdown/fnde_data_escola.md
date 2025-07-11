🗂️ Tabela fnde_data_escola
A tabela fnde_data_escola contém os dados cadastrais das escolas acompanhadas ou beneficiadas por programas do FNDE (como PNAE, PDDE e EEX). Ela funciona como referência principal para cruzamento de informações de adesão, repasses, matrícula e porte da escola.

| Campo                        | Tipo           | Restrição                     | Descrição                                                                                                               | Relacionamento com outras tabelas            |
| ---------------------------- | -------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `id`                         | `bigint`       | PK, auto\_increment, NOT NULL | Identificador único da escola dentro da base do FNDE. É usado como **chave primária**.                                  | 🔗 Relacionado com `fnde_data_eex.escola_id` |
| `codigo`                     | `varchar(20)`  | UNIQUE, NOT NULL              | Código oficial da escola, geralmente o **código INEP** ou outro identificador nacional. Garante unicidade.              | Pode ser cruzado com dados do MEC/INEP       |
| `nome`                       | `varchar(255)` | NOT NULL                      | Nome oficial da escola, como consta nos cadastros governamentais.                                                       | -                                            |
| `municipio`                  | `varchar(100)` | NOT NULL                      | Nome do município de localização da escola.                                                                             | Pode ser cruzado com `municipality_id`       |
| `uf`                         | `varchar(2)`   | NOT NULL                      | Sigla da unidade federativa (ex.: "BA", "SP").                                                                          | -                                            |
| `rede_ensino`                | `varchar(100)` | NULL                          | Rede administrativa da escola: "Municipal", "Estadual", "Federal", "Privada", etc.                                      | -                                            |
| `qtd_alunos_total`           | `int`          | NULL                          | Total de alunos matriculados. Utilizado para cálculos de repasse por aluno.                                             | -                                            |
| `qtd_alunos_ens_fundamental` | `int`          | NULL                          | Número de alunos no Ensino Fundamental (1º ao 9º ano).                                                                  | -                                            |
| `qtd_alunos_pre_escolar`     | `int`          | NULL                          | Número de alunos na Educação Infantil (Pré-escola).                                                                     | -                                            |
| `qtd_alunos_aee`             | `int`          | NULL                          | Quantidade de alunos atendidos pelo Atendimento Educacional Especializado (AEE), o que pode gerar repasses específicos. | -                                            |

🔗 Relacionamentos

| Campo    | Tabela Relacionada  | Tipo de Relacionamento           | Observação                                                                                   |
| -------- | ------------------- | -------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`     | `fnde_data_eex`     | FK (referenciado em `escola_id`) | Cada escola pode ter uma adesão única registrada ao programa EEX.                            |
| `codigo` | (MEC/INEP, externa) | Código institucional             | Pode ser usado para importar ou cruzar dados com cadastros oficiais do MEC ou Censo Escolar. |


### Índices
- Index em (`id`, `codigo`, `nome`, `municipio`,`uf`,`rede_ensino`,`qtd_alunos_total`,`qtd_alunos_ens_fundamental`,`qtd_alunos_pre_escolar`,`qtd_alunos_aee`) conforme definido em `Meta.indexes`.