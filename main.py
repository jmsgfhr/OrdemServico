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
ServiceLine1 = Frame( Service )
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

Labelpriority = Label(ServiceLine1, text = 'PRIORIDADE:')
Labelpriority.pack( side = LEFT )
PriorityOptionsMenu = OptionMenu( ServiceLine1, tkvar, *PriorityOptions )
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

tkvar = StringVar( Window )
PaymentOptions =  'A VISTA', 'PARCELADO'
tkvar.set('Escolha')

LabelPayment = Label(ServiceLine6, text = 'PAGAMENTO:')
LabelPayment.pack( side = LEFT )
PaymentOptionsMenu = OptionMenu( ServiceLine6, tkvar, *PaymentOptions )
PaymentOptionsMenu.pack( side = LEFT )

# opcoes de STATUS

tkvar = StringVar( Window )
PaymentStatus =  'ENVIADO', 'APROVADO', 'NAO APROVADO', 'PEDIDO', 'RECEBIDO', 'C/DEFEITO', 'RETIRADO', 'SAIU', 'DESCARTAR', 'NOVO', 'ENTRADA'
tkvar.set('Escolha')

PaymentStatusMenu = OptionMenu( ServiceLine6, tkvar, *PaymentStatus )
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
ButtonSave = Button( ServiceLine7 , text ="SALVAR", command = a )
ButtonSave.pack( side = RIGHT )

# Loop
Window.mainloop()