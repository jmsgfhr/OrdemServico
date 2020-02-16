from tkinter import  *
from datetime import datetime
import json
from functools import partial
from fpdf import Template

Today = datetime.now()

Window = Tk()

# Corpo do programa

# Funcoes

with open('database.json','r') as BD:
    database = json.load(BD)
BD.close()

def saveOrdem():
    ordem =  {
        "name": EntryName.get(),
        "certified": EntryCertified.get(),
        "phone": EntryPhone.get(),
        "email": EntryEmail.get(),
        "adress": EntryAdress.get(),
        "cep": EntryCEP.get(),
        "date": LabelDateShow['text'],
        "city": EntryCity.get(),
        "district": EntryDistrict.get(),
        "service": ServicePick.get(),
        "local": LocalPick.get(),
        "priority": PriorityPick.get(),
        "model": EntryModel.get(),
        "call": EntryCall.get(),
        "serialNumber": EntrySerialNumber.get(),
        "acesories": EntryAcessories.get(),
        "relatedProblem": EntryRelatedProblem.get(1.0,END),
        "problem": EntryProblem.get(1.0,END),
        "parts": EntryParts.get(1.0,END),
        "observations": EntryObservations.get(1.0,END),
        "payment": PaymentPick.get(),
        "status": StatusPick.get(),
        "servicePrice": EntryServicePrice.get(),
        "productPrice": EntryProductPrice.get()
        }    
    database.append(ordem)
    with open('database.json','w') as BD:
        json.dump(database,BD)
    BD.close()
    
    #creating pdf
    #this will define the ELEMENTS that will compose the template. 
    elements = [
        { 'name': 'company_logo', 'type': 'I', 'x1': 20.0, 'y1': 17.0, 'x2': 78.0, 'y2': 30.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 42, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Nome:', 'priority': 2, },
        { 'name': 'client_name', 'type': 'T', 'x1': 35.0, 'y1': 42, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 52, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'CPF/CNPJ:', 'priority': 2, },
        { 'name': 'client_certified', 'type': 'T', 'x1': 45.0, 'y1': 52, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 85.0, 'y1': 52, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Telefone:', 'priority': 2, },
        { 'name': 'client_phone', 'type': 'T', 'x1': 105, 'y1': 52, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 62, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'E-mail:', 'priority': 2, },
        { 'name': 'client_email', 'type': 'T', 'x1': 35.0, 'y1': 62, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 120, 'y1': 62, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Endereco:', 'priority': 2, },
        { 'name': 'client_adress', 'type': 'T', 'x1': 142, 'y1': 62, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'CEP:', 'priority': 2, },
        { 'name': 'client_cep', 'type': 'T', 'x1': 32.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 150.0, 'y1': 0, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Data:', 'priority': 2, },
        { 'name': 'date', 'type': 'T', 'x1': 161.0, 'y1': 0, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 55.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Cidade:', 'priority': 2, },
        { 'name': 'client_city', 'type': 'T', 'x1': 72.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 120.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Bairro:', 'priority': 2, },
        { 'name': 'client_district', 'type': 'T', 'x1': 135.0, 'y1': 72, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Servico:', 'priority': 2, },
        { 'name': 'service_type', 'type': 'T', 'x1': 37.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 70.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Local:', 'priority': 2, },
        { 'name': 'service_local', 'type': 'T', 'x1': 83.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 110.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Prioridade:', 'priority': 2, },
        { 'name': 'service_priority', 'type': 'T', 'x1': 133.0, 'y1': 102, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 112, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Modelo:', 'priority': 2, },
        { 'name': 'service_model', 'type': 'T', 'x1': 37.0, 'y1': 112, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 70, 'y1': 112, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Chamado:', 'priority': 2, },
        { 'name': 'service_call', 'type': 'T', 'x1': 92, 'y1': 112, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 122, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'N/S:', 'priority': 2, },
        { 'name': 'serial_number', 'type': 'T', 'x1': 29.0, 'y1': 122, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 83.0, 'y1': 122, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Acessorios:', 'priority': 2, },
        { 'name': 'acessories', 'type': 'T', 'x1': 108.0, 'y1': 122, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 132, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Problema Ralatado:', 'priority': 2, },
        { 'name': 'related_problem', 'type': 'T', 'x1': 20.0, 'y1': 142, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 152, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Problema Constatado:', 'priority': 2, },
        { 'name': 'problem', 'type': 'T', 'x1': 20.0, 'y1': 162, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 172, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Pecas:', 'priority': 2, },
        { 'name': 'service_parts', 'type': 'T', 'x1': 20.0, 'y1': 182, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 192, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Observacoes:', 'priority': 2, },
        { 'name': 'observation', 'type': 'T', 'x1': 20.0, 'y1': 202, 'x2': 25.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 250, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Pagamento:', 'priority': 2, },
        { 'name': 'payment_type', 'type': 'T', 'x1': 45.0, 'y1': 250, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 77.0, 'y1': 250, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Status:', 'priority': 2, },
        { 'name': 'status', 'type': 'T', 'x1': 92.0, 'y1': 250, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 20.0, 'y1': 262, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Servico(s):', 'priority': 2, },
        { 'name': 'service_value', 'type': 'T', 'x1': 42.0, 'y1': 262, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        
        { 'name': 'label', 'type': 'T', 'x1': 77.0, 'y1': 262, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'Produtos(s):', 'priority': 2, },
        { 'name': 'service_products', 'type': 'T', 'x1': 102.0, 'y1': 262, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    ]

    #here we instantiate the template and define the HEADER
    f = Template(format="A4", elements=elements,
                title="Ordem de Servico")
    f.add_page()
    
    #we FILL some of the fields of the template with the information we want
    #note we access the elements treating the template instance as a "dict"
    f["company_name"] = "Inova Service"
    f["company_logo"] = "img/logo.png"
    f["client_name"] = EntryName.get()
    f["client_certified"] = EntryCertified.get()
    f["client_phone"] = EntryPhone.get()
    f["client_email"] = EntryEmail.get()
    f["client_adress"] = EntryAdress.get()
    f["client_cep"] = EntryCEP.get()
    f["date"] = LabelDateShow['text']
    f["client_city"] = EntryCity.get()
    f["client_district"] = EntryDistrict.get()
    f["service_type"] = ServicePick.get()
    f["service_local"] = LocalPick.get()
    f["service_priority"] = PriorityPick.get()
    f["service_model"] = EntryModel.get()
    f["service_call"] = EntryCall.get()
    f["serial_number"] = EntrySerialNumber.get()
    f["acessories"] = EntryAcessories.get()
    f["related_problem"] = EntryRelatedProblem.get(1.0,END)
    f["problem"] = EntryProblem.get(1.0,END)
    f["service_parts"] = EntryParts.get(1.0,END)
    f["observation"] = EntryObservations.get(1.0,END)
    f["payment_type"] = PaymentPick.get()
    f["status"] = StatusPick.get()
    f["service_value"] = EntryServicePrice.get()
    f["service_products"] = EntryProductPrice.get()

    #and now we render the page
    f.render("./Servico.pdf")

# Area do usuario

User = Frame(Window)
User.pack( side = TOP )
UserLine1 = Frame(User)
UserLine1.pack( side = TOP )
LabelName = Label(UserLine1, text="Nome:")
LabelName.pack( side = LEFT )
EntryName = Entry(UserLine1, bd = 1)
EntryName.pack( side = LEFT )
LabelCertified = Label(UserLine1, text="CNPJ/CPF:")
LabelCertified.pack( side = LEFT )
EntryCertified = Entry(UserLine1, bd = 1)
EntryCertified.pack( side = LEFT )
LabelPhone = Label(UserLine1, text="TELEFONE:")
LabelPhone.pack( side = LEFT )
EntryPhone = Entry(UserLine1, bd = 1)
EntryPhone.pack( side = LEFT )

UserLine2 = Frame(User)
UserLine2.pack( side = TOP )
LabelEmail = Label(UserLine2, text="EMAIL:")
LabelEmail.pack( side = LEFT )
EntryEmail = Entry(UserLine2, bd = 1)
EntryEmail.pack( side = LEFT )
LabelAdress = Label(UserLine2, text="ENDERECO:")
LabelAdress.pack( side = LEFT )
EntryAdress = Entry(UserLine2, bd = 1)
EntryAdress.pack( side = LEFT )
LabelCEP = Label(UserLine2, text="CEP:")
LabelCEP.pack( side = LEFT )
EntryCEP = Entry(UserLine2, bd = 1)
EntryCEP.pack( side = LEFT )

UserLine3 = Frame(User)
UserLine3.pack( side = TOP )
LabelDate = Label(UserLine3, text="DATA:")
LabelDate.pack( side = LEFT )
LabelDateShow = Label(UserLine3, text= str(Today.day)+"/"+str(Today.month)+"/"+str(Today.year))
LabelDateShow.pack( side = LEFT )
LabelCity = Label(UserLine3, text="CIDADE/UF:")
LabelCity.pack( side = LEFT )
EntryCity = Entry(UserLine3, bd = 1)
EntryCity.pack( side = LEFT )
LabelDistrict = Label(UserLine3, text="BAIRRO:")
LabelDistrict.pack( side = LEFT )
EntryDistrict = Entry(UserLine3, bd = 1)
EntryDistrict.pack( side = LEFT )

# Area do servico

Service = Frame( Window )
Service.pack( side = TOP )
ServiceLine1 = Frame( Service )
ServiceLine1.pack( side = TOP )

# Opcoes de servico
ServicePick = StringVar( Window )
ServiceOptions = { 'INSTALACAO','REPARO' }
ServicePick.set('Escolha')

LabelService = Label(ServiceLine1, text = 'SERVICO:')
LabelService.pack( side = LEFT )
ServiceOptionsMenu = OptionMenu( ServiceLine1, ServicePick, *ServiceOptions )
ServiceOptionsMenu.pack( side = LEFT )

# Opcoes de local
LocalPick = StringVar( Window )
LocalOptions = { 'INTERNO','EXTERNO' }
LocalPick.set('Escolha')

LabelLocal = Label(ServiceLine1, text = 'LOCAL:')
LabelLocal.pack( side = LEFT )
LocalOptionsMenu = OptionMenu( ServiceLine1, LocalPick, *LocalOptions )
LocalOptionsMenu.pack( side = LEFT )

# Opcoes de prioridade
PriorityPick = StringVar( Window )
PriorityOptions =  'BAIXA','NORMAL','ALTA','URGENTE' 
PriorityPick.set('Escolha')

Labelpriority = Label(ServiceLine1, text = 'PRIORIDADE:')
Labelpriority.pack( side = LEFT )
PriorityOptionsMenu = OptionMenu( ServiceLine1, PriorityPick, *PriorityOptions )
PriorityOptionsMenu.pack( side = LEFT )

ServiceLine2 = Frame( Service )
ServiceLine2.pack( side = TOP )
LabelModel = Label(ServiceLine2, text="MODELO:")
LabelModel.pack( side = LEFT )
EntryModel = Entry(ServiceLine2, bd = 1)
EntryModel.pack( side = LEFT )
EntryCall = Entry(ServiceLine2, bd = 1)
EntryCall.pack( side = RIGHT )
LabelCall = Label(ServiceLine2, text="CHAMADO:")
LabelCall.pack( side = RIGHT )

ServiceLine3 = Frame( Service )
ServiceLine3.pack( side = TOP )
LabelSerialNumber = Label(ServiceLine3, text="N/S:")
LabelSerialNumber.pack( side = LEFT )
EntrySerialNumber = Entry(ServiceLine3, bd = 1)
EntrySerialNumber.pack( side = LEFT )
EntryAcessories = Entry(ServiceLine3, bd = 1)
EntryAcessories.pack( side = RIGHT )
LabelAcessories = Label(ServiceLine3, text="ACESSORIOS:")
LabelAcessories.pack( side = RIGHT )

ServiceLine4 = Frame( Service )
ServiceLine4.pack( side = TOP )

ServiceRelatedProblem = Frame( ServiceLine4 )
ServiceRelatedProblem.pack( side = LEFT )
LabelRelatedProblem = Label( ServiceRelatedProblem, text="PROBLEMA RELATADO:")
LabelRelatedProblem.pack()
EntryRelatedProblem = Text( ServiceRelatedProblem, width = 30 , height = 8 )
EntryRelatedProblem.pack()

ServiceProblem = Frame( ServiceLine4 )
ServiceProblem.pack( side = RIGHT )
LabelProblem = Label( ServiceProblem, text="PROBLEMA CONSTATADO:")
LabelProblem.pack()
EntryProblem = Text( ServiceProblem, width = 30 , height = 8 )
EntryProblem.pack()

ServiceLine5 = Frame( Service )
ServiceLine5.pack( side = TOP )

ServiceParts = Frame( ServiceLine5 )
ServiceParts.pack( side = LEFT )
LabelParts = Label( ServiceParts, text="PECAS:")
LabelParts.pack()
EntryParts = Text( ServiceParts, width = 30 , height = 8 )
EntryParts.pack()

ServiceObservations = Frame( ServiceLine5 )
ServiceObservations.pack( side = RIGHT )
LabelObservations = Label( ServiceObservations, text="OBS:")
LabelObservations.pack()
EntryObservations = Text( ServiceObservations, width = 30 , height = 8 )
EntryObservations.pack()

ServiceLine6 = Frame( Service )
ServiceLine6.pack( side = TOP )

# opcoes de pagamento

PaymentPick = StringVar( Window )
PaymentOptions =  'A VISTA', 'PARCELADO'
PaymentPick.set('Escolha')

LabelPayment = Label(ServiceLine6, text = 'PAGAMENTO:')
LabelPayment.pack( side = LEFT )
PaymentOptionsMenu = OptionMenu( ServiceLine6, PaymentPick, *PaymentOptions )
PaymentOptionsMenu.pack( side = LEFT )

# opcoes de STATUS

StatusPick = StringVar( Window )
PaymentStatus =  'ENVIADO', 'APROVADO', 'NAO APROVADO', 'PEDIDO', 'RECEBIDO', 'C/DEFEITO', 'RETIRADO', 'SAIU', 'DESCARTAR', 'NOVO', 'ENTRADA'
StatusPick.set('Escolha')

PaymentStatusMenu = OptionMenu( ServiceLine6, StatusPick, *PaymentStatus )
PaymentStatusMenu.pack( side = RIGHT )
LabelStatus = Label(ServiceLine6, text = 'STATUS:')
LabelStatus.pack( side = RIGHT )

ServiceLine7 = Frame( Service )
ServiceLine7.pack( side = TOP )

LabelServicePrice = Label(ServiceLine7, text="VALORES - SERVICO(S):")
LabelServicePrice.pack( side = LEFT )
EntryServicePrice = Entry(ServiceLine7, bd = 1)
EntryServicePrice.pack( side = LEFT )
LabelProductPrice = Label(ServiceLine7, text="PRODUTO(S):")
LabelProductPrice.pack( side = LEFT )
EntryProductPrice = Entry(ServiceLine7, bd = 1)
EntryProductPrice.pack( side = LEFT )
ButtonSave = Button( ServiceLine7 , text ="SALVAR", command = saveOrdem)
ButtonSave.pack( side = RIGHT )

# Loop
Window.mainloop()