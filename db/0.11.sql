 -- admin user
INSERT INTO public.users(username, name, surname, email, password, admin) VALUES ('admin', 'admin', 'admin', 'admin', '$2b$12$JJnDP/YkLln366KbQfQsb.IrI2Gih5jYI/BTx.XZocyWojXt1luby', true);

alter table public.metadata add column image character varying (255)
alter table public.metadata add column segmentation character varying (255)