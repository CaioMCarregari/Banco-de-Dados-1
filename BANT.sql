--
-- PostgreSQL database dump
--

-- Dumped from database version 14.18 (Ubuntu 14.18-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 17.5

-- Started on 2025-07-06 20:18:58 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 16541)
-- Name: carona; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carona (
    id_carona integer NOT NULL,
    origem character varying(100),
    destino character varying(100),
    distancia_km numeric,
    duracao_minutos integer,
    id_motorista integer NOT NULL,
    id_veiculo integer NOT NULL
);


ALTER TABLE public.carona OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16540)
-- Name: carona_id_carona_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.carona_id_carona_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.carona_id_carona_seq OWNER TO postgres;

--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 215
-- Name: carona_id_carona_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.carona_id_carona_seq OWNED BY public.carona.id_carona;


--
-- TOC entry 210 (class 1259 OID 16507)
-- Name: motoristas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.motoristas (
    id_motorista integer NOT NULL,
    cnh character varying(11) NOT NULL,
    nome character varying(50)
);


ALTER TABLE public.motoristas OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16506)
-- Name: motoristas_id_motorista_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.motoristas_id_motorista_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.motoristas_id_motorista_seq OWNER TO postgres;

--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 209
-- Name: motoristas_id_motorista_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.motoristas_id_motorista_seq OWNED BY public.motoristas.id_motorista;


--
-- TOC entry 219 (class 1259 OID 16623)
-- Name: pagamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pagamento (
    id_pagamento integer NOT NULL,
    valor numeric(10,2) NOT NULL
);


ALTER TABLE public.pagamento OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16622)
-- Name: pagamento_id_pagamento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pagamento_id_pagamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pagamento_id_pagamento_seq OWNER TO postgres;

--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 218
-- Name: pagamento_id_pagamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pagamento_id_pagamento_seq OWNED BY public.pagamento.id_pagamento;


--
-- TOC entry 220 (class 1259 OID 16629)
-- Name: pagar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pagar (
    id_passageiro integer NOT NULL,
    id_pagamento integer NOT NULL,
    data_hora_pagamento timestamp without time zone NOT NULL
);


ALTER TABLE public.pagar OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16525)
-- Name: passageiros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.passageiros (
    id_passageiro integer NOT NULL,
    cpf character varying(11) NOT NULL,
    nome character varying(50)
);


ALTER TABLE public.passageiros OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16524)
-- Name: passageiros_id_passageiro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.passageiros_id_passageiro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.passageiros_id_passageiro_seq OWNER TO postgres;

--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 213
-- Name: passageiros_id_passageiro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.passageiros_id_passageiro_seq OWNED BY public.passageiros.id_passageiro;


--
-- TOC entry 217 (class 1259 OID 16559)
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    id_passageiro integer NOT NULL,
    id_carona integer NOT NULL,
    data_hora_pedido timestamp without time zone
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16644)
-- Name: recebe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recebe (
    id_motorista integer NOT NULL,
    id_pagamento integer NOT NULL,
    data_recebe date
);


ALTER TABLE public.recebe OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16516)
-- Name: veiculos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.veiculos (
    id_veiculo integer NOT NULL,
    modelo character varying(30) NOT NULL,
    placa character varying(7) NOT NULL,
    ano integer,
    cor character varying(20),
    capacidade_passageiro smallint,
    id_motorista integer
);


ALTER TABLE public.veiculos OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16515)
-- Name: veiculos_id_veiculo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.veiculos_id_veiculo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.veiculos_id_veiculo_seq OWNER TO postgres;

--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 211
-- Name: veiculos_id_veiculo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.veiculos_id_veiculo_seq OWNED BY public.veiculos.id_veiculo;


--
-- TOC entry 3244 (class 2604 OID 16544)
-- Name: carona id_carona; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carona ALTER COLUMN id_carona SET DEFAULT nextval('public.carona_id_carona_seq'::regclass);


--
-- TOC entry 3241 (class 2604 OID 16510)
-- Name: motoristas id_motorista; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.motoristas ALTER COLUMN id_motorista SET DEFAULT nextval('public.motoristas_id_motorista_seq'::regclass);


--
-- TOC entry 3245 (class 2604 OID 16626)
-- Name: pagamento id_pagamento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagamento ALTER COLUMN id_pagamento SET DEFAULT nextval('public.pagamento_id_pagamento_seq'::regclass);


--
-- TOC entry 3243 (class 2604 OID 16528)
-- Name: passageiros id_passageiro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passageiros ALTER COLUMN id_passageiro SET DEFAULT nextval('public.passageiros_id_passageiro_seq'::regclass);


--
-- TOC entry 3242 (class 2604 OID 16519)
-- Name: veiculos id_veiculo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.veiculos ALTER COLUMN id_veiculo SET DEFAULT nextval('public.veiculos_id_veiculo_seq'::regclass);


--
-- TOC entry 3427 (class 0 OID 16541)
-- Dependencies: 216
-- Data for Name: carona; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.carona (id_carona, origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo) FROM stdin;
\.


--
-- TOC entry 3421 (class 0 OID 16507)
-- Dependencies: 210
-- Data for Name: motoristas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.motoristas (id_motorista, cnh, nome) FROM stdin;
\.


--
-- TOC entry 3430 (class 0 OID 16623)
-- Dependencies: 219
-- Data for Name: pagamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pagamento (id_pagamento, valor) FROM stdin;
\.


--
-- TOC entry 3431 (class 0 OID 16629)
-- Dependencies: 220
-- Data for Name: pagar; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pagar (id_passageiro, id_pagamento, data_hora_pagamento) FROM stdin;
\.


--
-- TOC entry 3425 (class 0 OID 16525)
-- Dependencies: 214
-- Data for Name: passageiros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.passageiros (id_passageiro, cpf, nome) FROM stdin;
\.


--
-- TOC entry 3428 (class 0 OID 16559)
-- Dependencies: 217
-- Data for Name: pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedido (id_passageiro, id_carona, data_hora_pedido) FROM stdin;
\.


--
-- TOC entry 3432 (class 0 OID 16644)
-- Dependencies: 221
-- Data for Name: recebe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recebe (id_motorista, id_pagamento, data_recebe) FROM stdin;
\.


--
-- TOC entry 3423 (class 0 OID 16516)
-- Dependencies: 212
-- Data for Name: veiculos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.veiculos (id_veiculo, modelo, placa, ano, cor, capacidade_passageiro, id_motorista) FROM stdin;
\.


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 215
-- Name: carona_id_carona_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.carona_id_carona_seq', 1, false);


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 209
-- Name: motoristas_id_motorista_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.motoristas_id_motorista_seq', 1, false);


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 218
-- Name: pagamento_id_pagamento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pagamento_id_pagamento_seq', 1, false);


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 213
-- Name: passageiros_id_passageiro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.passageiros_id_passageiro_seq', 1, false);


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 211
-- Name: veiculos_id_veiculo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.veiculos_id_veiculo_seq', 1, false);


--
-- TOC entry 3259 (class 2606 OID 16548)
-- Name: carona carona_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carona
    ADD CONSTRAINT carona_pkey PRIMARY KEY (id_carona);


--
-- TOC entry 3247 (class 2606 OID 16607)
-- Name: motoristas motoristas_cnh_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.motoristas
    ADD CONSTRAINT motoristas_cnh_key UNIQUE (cnh);


--
-- TOC entry 3249 (class 2606 OID 16512)
-- Name: motoristas motoristas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.motoristas
    ADD CONSTRAINT motoristas_pkey PRIMARY KEY (id_motorista);


--
-- TOC entry 3263 (class 2606 OID 16628)
-- Name: pagamento pagamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagamento
    ADD CONSTRAINT pagamento_pkey PRIMARY KEY (id_pagamento);


--
-- TOC entry 3265 (class 2606 OID 24815)
-- Name: pagar pagar_id_pagamento_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagar
    ADD CONSTRAINT pagar_id_pagamento_unique UNIQUE (id_pagamento);


--
-- TOC entry 3267 (class 2606 OID 16633)
-- Name: pagar pagar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagar
    ADD CONSTRAINT pagar_pkey PRIMARY KEY (id_passageiro, id_pagamento);


--
-- TOC entry 3255 (class 2606 OID 16616)
-- Name: passageiros passageiros_cpf_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passageiros
    ADD CONSTRAINT passageiros_cpf_key UNIQUE (cpf);


--
-- TOC entry 3257 (class 2606 OID 16530)
-- Name: passageiros passageiros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passageiros
    ADD CONSTRAINT passageiros_pkey PRIMARY KEY (id_passageiro);


--
-- TOC entry 3261 (class 2606 OID 16563)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id_passageiro, id_carona);


--
-- TOC entry 3269 (class 2606 OID 24817)
-- Name: recebe recebe_id_pagamento_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recebe
    ADD CONSTRAINT recebe_id_pagamento_unique UNIQUE (id_pagamento);


--
-- TOC entry 3271 (class 2606 OID 16648)
-- Name: recebe recebe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recebe
    ADD CONSTRAINT recebe_pkey PRIMARY KEY (id_motorista, id_pagamento);


--
-- TOC entry 3251 (class 2606 OID 16521)
-- Name: veiculos veiculos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.veiculos
    ADD CONSTRAINT veiculos_pkey PRIMARY KEY (id_veiculo);


--
-- TOC entry 3253 (class 2606 OID 16523)
-- Name: veiculos veiculos_placa_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.veiculos
    ADD CONSTRAINT veiculos_placa_key UNIQUE (placa);


--
-- TOC entry 3273 (class 2606 OID 16549)
-- Name: carona carona_id_motorista_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carona
    ADD CONSTRAINT carona_id_motorista_fkey FOREIGN KEY (id_motorista) REFERENCES public.motoristas(id_motorista);


--
-- TOC entry 3274 (class 2606 OID 16554)
-- Name: carona carona_id_veiculo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carona
    ADD CONSTRAINT carona_id_veiculo_fkey FOREIGN KEY (id_veiculo) REFERENCES public.veiculos(id_veiculo);


--
-- TOC entry 3277 (class 2606 OID 16639)
-- Name: pagar pagar_id_pagamento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagar
    ADD CONSTRAINT pagar_id_pagamento_fkey FOREIGN KEY (id_pagamento) REFERENCES public.pagamento(id_pagamento);


--
-- TOC entry 3278 (class 2606 OID 16634)
-- Name: pagar pagar_id_passageiro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagar
    ADD CONSTRAINT pagar_id_passageiro_fkey FOREIGN KEY (id_passageiro) REFERENCES public.passageiros(id_passageiro);


--
-- TOC entry 3275 (class 2606 OID 16569)
-- Name: pedido pedido_id_carona_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_id_carona_fkey FOREIGN KEY (id_carona) REFERENCES public.carona(id_carona);


--
-- TOC entry 3276 (class 2606 OID 16564)
-- Name: pedido pedido_id_passageiro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_id_passageiro_fkey FOREIGN KEY (id_passageiro) REFERENCES public.passageiros(id_passageiro);


--
-- TOC entry 3279 (class 2606 OID 16649)
-- Name: recebe recebe_id_motorista_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recebe
    ADD CONSTRAINT recebe_id_motorista_fkey FOREIGN KEY (id_motorista) REFERENCES public.motoristas(id_motorista);


--
-- TOC entry 3280 (class 2606 OID 16654)
-- Name: recebe recebe_id_pagamento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recebe
    ADD CONSTRAINT recebe_id_pagamento_fkey FOREIGN KEY (id_pagamento) REFERENCES public.pagamento(id_pagamento);


--
-- TOC entry 3272 (class 2606 OID 16659)
-- Name: veiculos veiculos_motorista; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.veiculos
    ADD CONSTRAINT veiculos_motorista FOREIGN KEY (id_motorista) REFERENCES public.motoristas(id_motorista);


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2025-07-06 20:18:58 -03

--
-- PostgreSQL database dump complete
--

