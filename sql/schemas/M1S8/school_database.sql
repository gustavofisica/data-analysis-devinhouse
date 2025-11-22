-- ================================================================
-- Complete Database Script - School Management System
-- Module: M1S8
-- Author: Luis Gustavo de Matos dos Santos
-- Date: 22/11/2025
-- ================================================================
-- This script creates a complete school database with:
-- - 6 related tables (Matricula, Turma, Sala, Aluno, Professor, Disciplina)
-- - Relationships: Matriculado, Alocada, Supervisiona, Possui, Leciona
-- - Full CRUD operations (CREATE, INSERT, UPDATE, DELETE)
-- - Complex queries with filters and ordering
-- ================================================================

-- ================================================================
-- PART 0: CREATE DATABASE
-- ================================================================

DROP DATABASE IF EXISTS "DEVinHouseSchool";
CREATE DATABASE "DEVinHouseSchool";

-- ================================================================
-- PART 1: DROP TABLES (Clean existing structure)
-- ================================================================

DROP TABLE IF EXISTS turma_disciplina CASCADE;
DROP TABLE IF EXISTS matricula CASCADE;
DROP TABLE IF EXISTS turma CASCADE;
DROP TABLE IF EXISTS sala CASCADE;
DROP TABLE IF EXISTS aluno CASCADE;
DROP TABLE IF EXISTS professor CASCADE;
DROP TABLE IF EXISTS disciplina CASCADE;

-- ================================================================
-- PART 2: CREATE TABLES (DDL)
-- ================================================================

CREATE TABLE aluno (
    ra VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL
);

CREATE TABLE sala (
    numero INTEGER PRIMARY KEY,
    predio VARCHAR(50) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE turma (
    id_turma INTEGER PRIMARY KEY,
    horario VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    numero_sala INTEGER NOT NULL,
    CONSTRAINT fk_turma_sala 
        FOREIGN KEY (numero_sala) 
        REFERENCES sala(numero)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE matricula (
    situacao VARCHAR(20) NOT NULL,
    data DATE NOT NULL,
    nota DECIMAL(4, 2),
    ra_aluno VARCHAR(20) NOT NULL,
    id_turma INTEGER NOT NULL,
    PRIMARY KEY (ra_aluno, id_turma),
    CONSTRAINT fk_matricula_aluno 
        FOREIGN KEY (ra_aluno) 
        REFERENCES aluno(ra)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_matricula_turma 
        FOREIGN KEY (id_turma) 
        REFERENCES turma(id_turma)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_nota CHECK (nota >= 0 AND nota <= 10),
    CONSTRAINT chk_situacao CHECK (situacao IN ('Matriculado', 'Aprovado', 'Reprovado', 'Cursando'))
);

CREATE TABLE professor (
    matricula VARCHAR(20) PRIMARY KEY,
    data_admissao DATE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100)
);

CREATE TABLE disciplina (
    id_disciplina INTEGER PRIMARY KEY,
    credito INTEGER NOT NULL CHECK (credito > 0),
    nome VARCHAR(100) NOT NULL,
    carga_horaria INTEGER NOT NULL CHECK (carga_horaria > 0)
);

CREATE TABLE turma_disciplina (
    data_cadastro DATE NOT NULL,
    id_turma INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    matricula_professor VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_turma, id_disciplina),
    CONSTRAINT fk_td_turma 
        FOREIGN KEY (id_turma) 
        REFERENCES turma(id_turma)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_td_disciplina 
        FOREIGN KEY (id_disciplina) 
        REFERENCES disciplina(id_disciplina)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_td_professor 
        FOREIGN KEY (matricula_professor) 
        REFERENCES professor(matricula)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE INDEX idx_matricula_aluno ON matricula(ra_aluno);
CREATE INDEX idx_matricula_turma ON matricula(id_turma);
CREATE INDEX idx_turma_sala ON turma(numero_sala);
CREATE INDEX idx_td_turma ON turma_disciplina(id_turma);
CREATE INDEX idx_td_disciplina ON turma_disciplina(id_disciplina);
CREATE INDEX idx_td_professor ON turma_disciplina(matricula_professor);

-- ================================================================
-- PART 3: INSERT DATA (DML - INSERT)
-- ================================================================

INSERT INTO aluno (ra, nome, cpf) VALUES
('2024001', 'Ana Silva Santos', '12345678901'),
('2024002', 'Bruno Costa Lima', '23456789012'),
('2024003', 'Carlos Eduardo Souza', '34567890123'),
('2024004', 'Diana Ferreira Alves', '45678901234'),
('2024005', 'Eduardo Pereira Gomes', '56789012345');

INSERT INTO sala (numero, predio, nome) VALUES
(101, 'Bloco A', 'Laboratório de Informática 1'),
(102, 'Bloco A', 'Sala de Aula Teórica 1'),
(201, 'Bloco B', 'Laboratório de Física'),
(202, 'Bloco B', 'Sala de Aula Teórica 2'),
(301, 'Bloco C', 'Auditório Principal');

INSERT INTO turma (id_turma, horario, data, numero_sala) VALUES
(1, '08:00-10:00', '2025-02-01', 101),
(2, '10:00-12:00', '2025-02-01', 102),
(3, '14:00-16:00', '2025-02-01', 201),
(4, '16:00-18:00', '2025-02-01', 202),
(5, '19:00-21:00', '2025-02-01', 301);

INSERT INTO professor (matricula, data_admissao, nome, especialidade) VALUES
('PROF001', '2020-01-15', 'Dr. João Pedro Oliveira', 'Banco de Dados'),
('PROF002', '2019-03-20', 'Dra. Maria Fernanda Costa', 'Programação'),
('PROF003', '2021-08-10', 'Dr. Roberto Carlos Silva', 'Matemática'),
('PROF004', '2018-05-25', 'Dra. Patricia Lima Santos', 'Física'),
('PROF005', '2022-01-30', 'Dr. Lucas Almeida Rocha', 'Engenharia de Software');

INSERT INTO disciplina (id_disciplina, credito, nome, carga_horaria) VALUES
(1, 4, 'Banco de Dados I', 80),
(2, 4, 'Programação Orientada a Objetos', 80),
(3, 3, 'Cálculo I', 60),
(4, 3, 'Física I', 60),
(5, 4, 'Engenharia de Software', 80);

INSERT INTO matricula (situacao, data, nota, ra_aluno, id_turma) VALUES
('Aprovado', '2025-02-01', 8.5, '2024001', 1),
('Aprovado', '2025-02-01', 9.0, '2024001', 2),
('Aprovado', '2025-02-01', 7.5, '2024002', 1),
('Reprovado', '2025-02-01', 5.5, '2024003', 3),
('Cursando', '2025-02-01', 4.0, '2024004', 4),
('Reprovado', '2025-02-01', 3.5, '2024005', 5);

INSERT INTO turma_disciplina (data_cadastro, id_turma, id_disciplina, matricula_professor) VALUES
('2025-01-15', 1, 1, 'PROF001'),
('2025-01-15', 2, 2, 'PROF002'),
('2025-01-15', 3, 3, 'PROF003'),
('2025-01-15', 4, 4, 'PROF004'),
('2025-01-15', 5, 5, 'PROF005');

-- ================================================================
-- PART 4: UPDATE DATA (DML - UPDATE)
-- ================================================================

UPDATE aluno 
SET nome = 'Ana Silva Santos Oliveira'
WHERE ra = '2024001';

UPDATE sala 
SET nome = 'Laboratório de Informática Avançada'
WHERE numero = 101;

UPDATE turma 
SET horario = '08:00-11:00'
WHERE id_turma = 1;

UPDATE professor 
SET especialidade = 'Banco de Dados e Big Data'
WHERE matricula = 'PROF001';

UPDATE disciplina 
SET carga_horaria = 90
WHERE id_disciplina = 1;

UPDATE matricula 
SET nota = 9.5
WHERE ra_aluno = '2024002' AND id_turma = 1;

-- ================================================================
-- PART 5: DELETE DATA (DML - DELETE)
-- ================================================================

DELETE FROM matricula 
WHERE ra_aluno = '2024005' AND id_turma = 5;

DELETE FROM turma_disciplina 
WHERE id_turma = 5 AND id_disciplina = 5;

DELETE FROM turma 
WHERE id_turma = 5;

DELETE FROM disciplina 
WHERE id_disciplina = 5;

DELETE FROM professor 
WHERE matricula = 'PROF005';

DELETE FROM aluno 
WHERE ra = '2024005';

DELETE FROM sala 
WHERE numero = 301;

-- ================================================================
-- PART 6: QUERIES (DQL - SELECT with filters and ordering)
-- ================================================================

SELECT 
    a.ra,
    a.nome,
    COUNT(m.id_turma) AS total_turmas,
    COALESCE(AVG(m.nota), 0) AS media_notas
FROM aluno a
LEFT JOIN matricula m ON a.ra = m.ra_aluno
GROUP BY a.ra, a.nome
ORDER BY a.nome;

SELECT 
    t.id_turma,
    t.horario,
    s.predio,
    s.nome AS sala,
    d.nome AS disciplina,
    p.nome AS professor
FROM turma t
JOIN sala s ON t.numero_sala = s.numero
JOIN turma_disciplina td ON t.id_turma = td.id_turma
JOIN disciplina d ON td.id_disciplina = d.id_disciplina
JOIN professor p ON td.matricula_professor = p.matricula
ORDER BY t.id_turma;

SELECT 
    a.nome AS aluno,
    m.situacao,
    m.nota,
    d.nome AS disciplina
FROM matricula m
JOIN aluno a ON m.ra_aluno = a.ra
JOIN turma t ON m.id_turma = t.id_turma
JOIN turma_disciplina td ON t.id_turma = td.id_turma
JOIN disciplina d ON td.id_disciplina = d.id_disciplina
WHERE m.nota IS NOT NULL
  AND m.nota >= 7.0
ORDER BY m.nota DESC;

SELECT 
    p.nome AS professor,
    p.especialidade,
    COUNT(td.id_turma) AS total_turmas,
    STRING_AGG(d.nome, ', ') AS disciplinas
FROM professor p
LEFT JOIN turma_disciplina td ON p.matricula = td.matricula_professor
LEFT JOIN disciplina d ON td.id_disciplina = d.id_disciplina
GROUP BY p.matricula, p.nome, p.especialidade
HAVING COUNT(td.id_turma) > 0
ORDER BY total_turmas DESC;

SELECT 
    d.nome AS disciplina,
    d.credito,
    d.carga_horaria,
    COUNT(td.id_turma) AS total_turmas,
    COUNT(DISTINCT m.ra_aluno) AS total_alunos
FROM disciplina d
LEFT JOIN turma_disciplina td ON d.id_disciplina = td.id_disciplina
LEFT JOIN matricula m ON td.id_turma = m.id_turma
GROUP BY d.id_disciplina, d.nome, d.credito, d.carga_horaria
ORDER BY d.nome;

SELECT 
    s.predio,
    s.numero,
    s.nome AS sala,
    COUNT(t.id_turma) AS total_turmas
FROM sala s
LEFT JOIN turma t ON s.numero = t.numero_sala
GROUP BY s.numero, s.predio, s.nome
ORDER BY s.predio, s.numero;

SELECT 
    a.nome AS aluno,
    COUNT(CASE WHEN m.situacao = 'Cursando' THEN 1 END) AS cursando,
    COUNT(CASE WHEN m.situacao = 'Aprovado' THEN 1 END) AS aprovado,
    COUNT(CASE WHEN m.situacao = 'Reprovado' THEN 1 END) AS reprovado
FROM aluno a
LEFT JOIN matricula m ON a.ra = m.ra_aluno
GROUP BY a.ra, a.nome
ORDER BY a.nome;

SELECT 
    t.id_turma,
    t.horario,
    d.nome AS disciplina,
    p.nome AS professor,
    COUNT(m.ra_aluno) AS total_alunos,
    AVG(m.nota) AS media_turma
FROM turma t
JOIN turma_disciplina td ON t.id_turma = td.id_turma
JOIN disciplina d ON td.id_disciplina = d.id_disciplina
JOIN professor p ON td.matricula_professor = p.matricula
LEFT JOIN matricula m ON t.id_turma = m.id_turma
WHERE t.data >= '2025-01-01'
GROUP BY t.id_turma, t.horario, d.nome, p.nome
HAVING COUNT(m.ra_aluno) > 0
ORDER BY total_alunos DESC, media_turma DESC NULLS LAST;
