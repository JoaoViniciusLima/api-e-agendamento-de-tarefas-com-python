from agendamentosdb import agendamentos
from worker import worker
import time
import schedule
from datetime import datetime


class AgendamentoService: 
  def ativar_lembrete(id):
    for agendamento in agendamentos:
      if agendamento["id"] == id:
        print(agendamento["descrição"])
    return schedule.CancelJob

  def procurar_agendamentos():
    dia = datetime.today().weekday()
    for agendamento in agendamentos:
      if dia in agendamento["dias"]:
        horario = datetime.strptime(agendamento["horario"], '%H:%M:%S').time()
        schedule.every().day.at(str(horario)).do(
        AgendamentoService.ativar_lembrete,
        id=agendamento["id"])
        

  @worker
  def worker_agendamento():
    schedule.every().day.at("00:00").do(AgendamentoService.procurar_agendamentos)
    while True:
      schedule.run_pending()
      time.sleep(1)
  