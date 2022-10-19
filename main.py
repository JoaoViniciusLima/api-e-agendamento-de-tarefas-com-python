from service import AgendamentoService
from api import app
AgendamentoService.procurar_agendamentos()

AgendamentoService.worker_agendamento()

app.run(port=5000,host='localhost',debug=True,use_reloader=False)
