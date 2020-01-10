from tkinter import  *
from datetime import datetime

Today = datetime.now()
Window = Tk()
# Corpo do programa

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
ServiceLine1 = Frame( Window )
ServiceLine1.pack( side = TOP )

# Opcoes de servico
tkvar = StringVar( Window )
ServiceOptions = { 'INSTALACAO','REPARO' }
tkvar.set('Escolha')

LabelService = Label(ServiceLine1, text = 'SERVICO:')
LabelService.pack( side = LEFT )
ServiceOptionsMenu = OptionMenu( ServiceLine1, tkvar, *ServiceOptions )
ServiceOptionsMenu.pack( side = LEFT )

# Opcoes de local
tkvar = StringVar( Window )
LocalOptions = { 'INTERNO','EXTERNO' }
tkvar.set('Escolha')

LabelLocal = Label(ServiceLine1, text = 'LOCAL:')
LabelLocal.pack( side = LEFT )
LocalOptionsMenu = OptionMenu( ServiceLine1, tkvar, *LocalOptions )
LocalOptionsMenu.pack( side = LEFT )

# Opcoes de prioridade
tkvar = StringVar( Window )
PriorityOptions =  'BAIXA','NORMAL','ALTA','URGENTE' 
tkvar.set('Escolha')

LabelpRIORITY = Label(ServiceLine1, text = 'PRIORIDADE:')
LabelpRIORITY.pack( side = LEFT )
PriorityOptionsMenu = OptionMenu( ServiceLine1, tkvar, *PriorityOptions )
PriorityOptionsMenu.pack( side = LEFT )

# Loop
Window.mainloop()