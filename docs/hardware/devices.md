
```mermaid
block-beta
   columns 3
   
   block:Interface
       columns 1
       InterfaceTitle("<i><b>Interfaces</b><i/>")
       InterfaceDigital["<b>Digital Interface</b>\nQuantum circuits with discrete gates"] 
       space
       InterfaceAnalog["<b>Analog Interface</b>\n Continuous-time evolution with Hamiltonians"] 
       space
       InterfaceAtomic["<b>Atomic Interface</b>\nLight-matter interactions between lasers and ions"]
       space
    end
    
    block:IR
       columns 1
       IRTitle("<i><b>IRs</b><i/>")
       IRDigital["Quantum circuit IR\nopenQASM, LLVM+QIR"] 
       space
       IRAnalog["openQSIM"]
       space
       IRAtomic["openAPL"]
       space
    end
    
    block:Emulator
       columns 1
       EmulatorsTitle("<i><b>Classical Emulators</b><i/>")
       
       EmulatorDigital["Pennylane, Qiskit"] 
       space
       EmulatorAnalog["QuTiP, QuantumOptics.jl"]
       space
       EmulatorAtomic["TrICal, QuantumIon.jl"]
       space
    end
    
    space
    block:RealTime
       columns 1
       RealTimeTitle("<i><b>Real-Time</b><i/>")
       space
       RTSoftware["ARTIQ, DAX, OQDAX"] 
       space
       RTGateware["Sinara Real-Time Control"]
       space
       RTHardware["Lasers, Modulators, Photodetection, Ion Trap"]
       space
       RTApparatus["Trapped-Ion QPU (<sup>171</sup>Yt<sup>+</sup>, <sup>133</sup>Ba<sup>+</sup>)"]
       space
    end
    space
    
   InterfaceDigital --> IRDigital
   InterfaceAnalog --> IRAnalog
   InterfaceAtomic --> IRAtomic
   
   IRDigital --> IRAnalog
   IRAnalog --> IRAtomic
   
   IRDigital --> EmulatorDigital
   IRAnalog --> EmulatorAnalog
   IRAtomic --> EmulatorAtomic
   
   IRAtomic --> RealTimeTitle
   
   RTSoftware --> RTGateware
   RTGateware --> RTHardware
   RTHardware --> RTApparatus
   
   classDef title fill:#d6d4d4,stroke:#333,color:#333;
   classDef digital fill:#E7E08B,stroke:#333,color:#333;
   classDef analog fill:#E4E9B2,stroke:#333,color:#333;
   classDef atomic fill:#D2E4C4,stroke:#333,color:#333;
   classDef realtime fill:#B5CBB7,stroke:#333,color:#333;

    classDef highlight fill:#f2bbbb,stroke:#333,color:#333,stroke-dasharray: 5 5;

    class InterfaceTitle,IRTitle,EmulatorsTitle,RealTimeTitle title
    class InterfaceDigital,IRDigital,EmulatorDigital digital
    class InterfaceAnalog,IRAnalog,EmulatorAnalog analog
    class InterfaceAtomic,IRAtomic,EmulatorAtomic atomic
    class RTSoftware,RTGateware,RTHardware,RTApparatus realtime
    
    class RealTime highlight
```


### Bloodstone
* Ion species: <sup>171</sup>Yb<sup>+</sup>
* Target number of qubits: 30 – 50
* Trap architecture: Segmented Blade Trap
* SPAM individual addressing: DMD
* Coherent individual addressing with: Double-pass AOM + AOD

![Bloodstone - Vacuum Chamber & Trap 1](./img/bloodstone-trap1.png){: style="width:300px"}
![Bloodstone - Vacuum Chamber & Trap 2](./img/bloodstone-trap2.png){: style="width:300px"}

### Beryl
* Ion species: <sup>133</sup>Ba<sup>+</sup>, <sup>137</sup>Ba<sup>+</sup>, <sup>138</sup>Ba<sup>+</sup>
* Target number of qubits: 16
* Trap architecture: [Sandia National Laboratories Phoenix Trap (HOA 2.0 platform)](https://arxiv.org/abs/2009.02398)
* SPAM individual addressing: AOMs
* Coherent individual addressing: Laser written waveguide + AOMs

![Beryl - Vacuum Chamber & Trap](./img/beryl-trap.png){: style="width:600px"}

## Real-time Control System
The OQD stack builds on the [Sinara](https://m-labs.hk/experiment-control/sinara-core/) and [ARTIQ](https://m-labs.hk/artiq/) ecosystems for real-time control.

### Sinara
[Sinara](https://sinara-hw.github.io/) is an open-source hardware ecosystem originally designed for use in quantum physics experiments running the ARTIQ control software.
The hardware is also suitable for a broad range of laboratory and test & measurement applications.
It is licensed under CERN OHL v1.2.


### ARTIQ (Advanced Real-Time Infrastructure for Quantum)
[The Advanced Real-Time Infrastructure for Quantum physics framework](https://github.com/m-labs/artiq) is a software framework developed by M-Labs that provides Python bindings to the Sinara real-time signal generation and detection apparatus at the core of the electrical apparatus.
ARTIQ functions by exposing control of the individual channels of custom-specified Sinara hardware in the Python programming language.
The system maintains an internal clock and timeline.
Events specified programmatically by the user are applied to the timeline and sent to the Sinara hardware with a series of queues.
The Sinara hardware then executes the instructions with nanosecond precision on a series of FPGAs.

### DAX (Duke ARTIQ Extensions)
[The Duke ARTIQ Extensions (DAX)](https://gitlab.com/duke-artiq/dax) are additional tools and capabilities drawn from traditional software design principles for the ARTIQ framework.
ARTIQ allows low-level access to individual channels on the Sinara hardware.
DAX provides a framework for grouping channels into logical modules representing appropriate experimental apparatus abstractions and services that use those modules to perform regular, repeatable tasks.
