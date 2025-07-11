# 🗂️ Tabela: fnde_data_prefeitodirigente
A tabela fnde_data_prefeitodirigente armazena informações sobre os gestores públicos municipais relacionados à educação: o prefeito e o dirigente municipal de educação (DME), com vínculo ao respectivo município. É útil para consultas institucionais, controle de responsabilidades e identificação de gestores nas ações do FNDE e programas federais.

Essa tabela facilita a gestão de comunicações, envio de ofícios, validações de cadastro e cruzamento com outros sistemas federais.

📑 Estrutura da Tabela

| Campo                | Tipo           | Obrigatório | Observações                                                                                                                                                      |
| -------------------- | -------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **id**               | `bigint`       | Sim (PK)    | Identificador único do registro. Valor gerado automaticamente (`auto_increment`).                                                                                |
| **inuid**            | `int unsigned` | Sim         | Código identificador único interno (possivelmente o **ID do FNDE** ou do sistema SIOPE/SIMEC/SIGECON).                                                           |
| **municipio\_nome**  | `varchar(255)` | Sim         | Nome do município ao qual os gestores estão vinculados. Utilizado para exibição legível.                                                                         |
| **estado**           | `varchar(2)`   | Sim         | Sigla da Unidade Federativa (ex: "BA", "SP", "MG"). Permite agrupamentos por estado.                                                                             |
| **prefeito\_nome**   | `varchar(150)` | Sim         | Nome do(a) atual **prefeito(a)** do município.                                                                                                                   |
| **dirigente\_nome**  | `varchar(150)` | Sim         | Nome do(a) atual **Dirigente Municipal de Educação** (DME). Responsável pela pasta da educação.                                                                  |
| **municipality\_id** | `int unsigned` | Não         | Chave estrangeira que vincula este registro à tabela de municípios (como `fnde_data_municipiofnde`). Permite relacionar o gestor ao ID padronizado do município. |

🔗 Relacionamentos
municipality_id:

FK (chave estrangeira) para a tabela de municípios, provavelmente fnde_data_municipiofnde ou similar.

Permite relacionar o prefeito e o dirigente a um município padronizado por ID, facilitando cruzamento com outras bases FNDE.

### Índices
- Index em (`id`,`inuid`,`municipio_nome`,`estado`,`prefeito_nome`,`dirigente_nome`,`municipality_id`) conforme definido em `Meta.indexes`.