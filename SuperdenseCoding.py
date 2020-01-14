from qiskit import IBMQ, Aer
IBMQ.load_account()
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import plot_histogram


qr = QuantumRegister(2)
cr = ClassicalRegister(2)



superdense = QuantumCircuit(qr,cr)
superdense.h(qr[0])
superdense.cx(qr[0],qr[1])

superdense.z(qr[0]) 
superdense.x(qr[0])
superdense.barrier()

superdense.cx(qr[0], qr[1])
superdense.h(qr[0])
superdense.measure(qr[0], cr[0])
superdense.measure(qr[1], cr[1])

local_backend = Aer.get_backend('qasm_simulator') 
superdense_job = execute(superdense, local_backend) 
superdense_result = superdense_job.result()

data = superdense_result.get_counts(superdense)
print(data)
superdense.draw(output='mpl')
plot_histogram(data)
