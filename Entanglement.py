from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit import IBMQ
IBMQ.load_account()
from qiskit.tools.visualization import plot_histogram
backend = Aer.get_backend(name='qasm_simulator')

q=QuantumRegister(2)
c1=ClassicalRegister(1)
c2=ClassicalRegister(2)

bell=QuantumCircuit(q)
bell.h(q[0])
bell.cx(q[0], q[1])

measure1=QuantumCircuit(q,c1)
measure1.measure(q[0],c1[0])
bell1=bell+measure1
bell1.draw(output='mpl')

measure2=QuantumCircuit(q,c1)
measure2.h(q[0])
measure2.measure(q[0],c1[0])
bell2=bell+measure2
bell2.draw(output='mpl')

measure3=QuantumCircuit(q,c1)
measure3.measure(q[1],c1[0])
bell3=bell+measure3
bell3.draw(output='mpl')

measure4=QuantumCircuit(q,c1)
measure4.h(q[1])
measure4.measure(q[1],c1[0])
bell4=bell+measure4
bell4.draw(output='mpl')

measure5=QuantumCircuit(q,c2)
measure5.measure(q[0],c2[0])
measure5.measure(q[1],c2[0])
bell5=bell+measure5
bell5.draw(output='mpl')

measure6=QuantumCircuit(q,c2)
measure6.h(q[0])
measure6.h(q[1])
measure6.measure(q[0],c2[0])
measure6.measure(q[1],c2[0])
bell6=bell+measure6
bell6.draw(output='mpl')

circuits=[bell1,bell2,bell3,bell4,bell5,bell6]
job=execute(circuits,backend,shots=1000)
result=job.result()
plot_histogram(result.get_counts(bell1))
plot_histogram(result.get_counts(bell2))
plot_histogram(result.get_counts(bell3))
plot_histogram(result.get_counts(bell4))
plot_histogram(result.get_counts(bell5))
plot_histogram(result.get_counts(bell6))
