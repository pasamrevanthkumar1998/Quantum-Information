from qiskit import IBMQ, Aer
IBMQ.load_account()
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import plot_histogram


tq = QuantumRegister(3)
tc0 = ClassicalRegister(1)
tc1 = ClassicalRegister(1)
tc2 = ClassicalRegister(1)

teleport = QuantumCircuit(tq, tc0,tc1,tc2)
teleport.h(tq[1])
teleport.cx(tq[1], tq[2])

teleport.z(tq[0])

teleport.cx(tq[0], tq[1])
teleport.h(tq[0])
teleport.barrier()

teleport.measure(tq[0], tc0[0])
teleport.measure(tq[1], tc1[0])

teleport.z(tq[2]).c_if(tc0, 1)
teleport.x(tq[2]).c_if(tc1, 1)

teleport.measure(tq[2], tc2[0])



local_backend = Aer.get_backend('qasm_simulator') 
teleport_job = execute(teleport, local_backend) 
teleport_result = teleport_job.result()

data = teleport_result.get_counts(teleport)
print(data)
teleport.draw(output='mpl')
plot_histogram(data)
