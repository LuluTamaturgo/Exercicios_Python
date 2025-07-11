Tabela fnde_data_conselhomunicipal
Esta tabela armazena informações cadastrais e de acompanhamento dos Conselhos Municipais que atuam no controle social dos programas do FNDE (por exemplo, CACS‑FUNDEB, CACS‑PNAE ou conselhos do PDDE).
Abaixo você encontra a descrição detalhada de cada campo, incluindo propósito e possíveis valores:

Ela registra:

O status da análise do conselho;

Informações sobre o mandato vigente;

Dados de endereço e contato;

Informações do órgão responsável;

Rastreamento de mudanças e controle de auditoria.

📑 Estrutura da Tabela

| Campo                     | Tipo         | Chave            | Descrição                                                                            | Relacionamentos Possíveis                                   |
| ------------------------- | ------------ | ---------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| `id`                      | bigint       | PK, auto\_inc    | Identificador técnico único da linha. Utilizado para **joins internos e auditoria**. | FK técnica para tabelas auxiliares (auditoria, logs etc.).  |
| `nu_seq_conselho_analise` | int          | UNIQUE, NOT NULL | Número sequencial da análise mais recente do conselho.                               | Pode ser usado em tabelas de histórico ou auditoria.        |
| `nu_seq_conselho`         | int          | NOT NULL         | Identificador oficial do conselho no sistema SISCACS/FNDE.                           | FK lógica para tabelas de composição ou análise de membros. |
| `situacao_analise`        | varchar(255) | NOT NULL         | Descrição textual da situação da análise (Ex.: Aprovado, Reprovado).                 | -                                                           |
| `codigo_situacao_analise` | int          | NOT NULL         | Código numérico correspondente à `situacao_analise`.                                 | Usado para filtros e relatórios.                            |
| `ativo`                   | tinyint(1)   | NOT NULL         | Flag booleana (1 = ativo, 0 = inativo/extinto).                                      | Usado em filtros ativos no sistema.                         |
| `tipo_colegiado`          | varchar(10)  | NULL             | Tipo de colegiado (ex.: CACS, FME, etc).                                             | Pode ser cruzado com uma tabela de tipos de colegiado.      |
| `frequencia_reuniao`      | varchar(10)  | NULL             | Frequência das reuniões do conselho.                                                 | -                                                           |
| `data_analise`            | datetime(6)  | NULL             | Data e hora de início da análise do conselho.                                        | -                                                           |
| `data_conclusao_analise`  | datetime(6)  | NULL             | Data e hora de conclusão da análise.                                                 | -                                                           |
| `data_cadastro_mandato`   | datetime(6)  | NULL             | Data de cadastro do mandato atual no sistema.                                        | -                                                           |
| `data_inicio_mandato`     | datetime(6)  | NULL             | Data de início do mandato vigente.                                                   | -                                                           |
| `data_termino_mandato`    | datetime(6)  | NULL             | Data prevista de término do mandato.                                                 | -                                                           |
| `orgao_responsavel`       | varchar(255) | NULL             | Nome do órgão municipal responsável pelo conselho (ex.: Secretaria de Educação).     | -                                                           |
| `cnpj_orgao_responsavel`  | varchar(20)  | NULL             | CNPJ do órgão responsável.                                                           | Pode ser cruzado com `fnde_data_cnpjmunicipio.cnpj`.        |
| `endereco`                | varchar(255) | NULL             | Logradouro do conselho.                                                              | -                                                           |
| `numero_endereco`         | varchar(10)  | NULL             | Número do imóvel.                                                                    | -                                                           |
| `complemento_endereco`    | varchar(255) | NULL             | Complemento do endereço.                                                             | -                                                           |
| `bairro`                  | varchar(255) | NULL             | Bairro do conselho.                                                                  | -                                                           |
| `cep`                     | varchar(10)  | NULL             | CEP da sede do conselho.                                                             | -                                                           |
| `telefone`                | varchar(20)  | NULL             | Telefone principal do conselho.                                                      | -                                                           |
| `telefone_secundario`     | varchar(20)  | NULL             | Telefone alternativo.                                                                | -                                                           |
| `email`                   | varchar(254) | NULL             | E-mail institucional do conselho.                                                    | -                                                           |
| `site_conselho`           | varchar(200) | NULL             | URL do site do conselho.                                                             | -                                                           |
| `atualizado_em`           | datetime(6)  | NOT NULL         | Data/hora da última atualização dos dados.                                           | Usado para auditoria.                                       |
| `municipality_id`         | bigint       | UNIQUE, NOT NULL | Identificador do município relacionado.                                              | 🔗 **FK para `fnde_data_municipiofnde.id` ou equivalente**. |
| `codigo_situacao_mandato` | int          | NULL             | Código da situação do mandato (ex.: 1 = vigente, 2 = expirado, 3 = prorrogado).      | Tabela de domínio de situação de mandato.                   |
| `ent_fed_json`            | JSON         | NULL             | Bloco JSON com dados adicionais sobre a entidade federativa.                         | -                                                           |
| `justificativa`           | longtext     | NULL             | Justificativa em texto livre para prorrogação ou rejeição.                           | -                                                           |
| `nu_seq_mandato_conselho` | int          | NULL             | Número sequencial do mandato vigente.                                                | Pode ser usado em controle de histórico de mandatos.        |
| `orgao_resp_bairro`       | varchar(255) | NULL             | Bairro do órgão responsável.                                                         | -                                                           |
| `orgao_resp_cep`          | varchar(10)  | NULL             | CEP do órgão responsável.                                                            | -                                                           |
| `orgao_resp_endereco`     | varchar(255) | NULL             | Endereço do órgão responsável.                                                       | -                                                           |
| `orgao_resp_municipio`    | varchar(255) | NULL             | Município do órgão responsável (texto).                                              | -                                                           |
| `orgao_resp_numero`       | varchar(10)  | NULL             | Número do endereço do órgão responsável.                                             | -                                                           |
| `usuario_siscacs`         | int          | NULL             | ID do usuário no sistema SISCACS que fez o cadastro ou atualização.                  | Pode se relacionar com uma tabela de usuários SISCACS.      |


### Índices
- Index em (`id`, `nu_seq_conselho_analise`, `nu_seq_conselho`, `situacao_analise`, `codigo_situacao_analise`,`ativo`,`tipo_colegiado`,`frequencia_reuniao`,`data_analise`,`data_conclusao_analise`,`data_cadastro_mandato`,`data_inicio_mandato`,`data_termino_mandato`,`orgao_responsavel`,`cnpj_orgao_responsavel`,`endereco`,`numero_endereco`,`complemento_endereco`,`bairro`,`cep`,`telefone`,`telefone_secundario`,`email`,`site_conselho`,`atualizado_em`,`municipality_id`,`codigo_situacao_mandato`,`ent_fed_json`,`justificativa`,`nu_seq_mandato_conselho`,`orgao_resp_bairro`,`orgao_resp_cep`,`orgao_resp_endereco`,`orgao_resp_municipio`,`orgao_resp_numero`,`usuario_siscacs`) conforme definido em `Meta.indexes`.