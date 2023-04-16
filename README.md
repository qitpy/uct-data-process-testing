# Overview

**Descriptions**: We crawled Jobs data from some websites. But we have an issues:  
**`Job structure in every job file is different with each others.`**

All we need from Job data is about these fields:

- **Job minimum requirement**: refer to the qualifications, skills, and experience that are necessary for an individual to perform a specific job
- **Job preferred requirement**: refer to any other reference from job. ex: "nice to have",...
- **Job responsibilities**: refer to the specific duties and tasks that an employee is expected to perform as part of their job
- **Job compensation**: refers to the total amount of pay and benefits that an employer provides to an employee in exchange for their work.
- **Job about**: any other information that is the rest - we want to collect as much as possible the data

---

# Example

### Input:

```text
## Job Description

#### Description

As our DevOps Engineer, you will be helping us build and maintain blockchain
networks and protocols. You will work on improving our current infrastructure
including security, automation, and monitoring among other things. You will
also have the chance to dive deep into new blockchain protocols, run testnets,
build secure and scalable infra and maintain it.

### What will you do?

  * Build secure and reliable infrastructure to monitor, detect and mitigate performance and security issues
  * System administration activities for Linux servers, which includes routine, proactive daily management of the health, stability, and availability of system infrastructure
  * Create and maintain system procedural and technical documentation
  * Stay up to date and build on peer-to-peer networking security best practices
  * Create, maintain and communicate threat models + risk assessments for all systems we operate

### What excites us about you?

  * You have experience as DevOps/SRE/Infrastructure engineer
  * You have experience managing server infrastructures with high availability requirements
  * You had designed secure networks, systems, and application architectures
  * You had set up and maintained software in both data centers and cloud environments
  * You have a deep understanding of sockets, full networking stack, and Linux security
  * You possess the knowledge of building automation and CI/CD processes and tools
  * You are experienced with Docker, Kubernetes, and other cloud deployment technologies
  * You have flexibility, teamwork, and you are comfortable with ambiguity, able to take charge and get things done despite the unknowns

### What will be great to have?

  * You have an understanding of the blockchain space and blockchain technology
  * You possess knowledge of cryptography and security best practices
  * You have contributions to open source communities

If those describe you, this is the right opportunity for you!

### Why are we awesome you ask?

We are a truly global team! We are digital nomads coming from more than 12
different countries, working from wherever we want. We have a collective
mission, to provide meaningful services and bring a unique value to users
within the crypto space.

We are looking for fun, curious, and committed individuals to swim with us!

#### Requirements

  * A BSc/BA degree in Computer Science or a relevant field

Listed in: [Web3 Jobs](https://cryptojobslist.com), [Devops Web3
Jobs](https://cryptojobslist.com/devops), [Security Web3
Jobs](https://cryptojobslist.com/security), [Sre Web3
Jobs](https://cryptojobslist.com/sre), [Full Time Web3
Jobs](https://cryptojobslist.com/full-time), [Remote Usa Web3
Jobs](https://cryptojobslist.com/remote-usa), [Developer Crypto
Jobs](https://cryptojobslist.com/developer).
```

### Expected output:

```json
{
    "about": "
        #### Description
        As our DevOps Engineer, you will be helping us build and maintain blockchain
        networks and protocols. You will work on improving our current infrastructure
        including security, automation, and monitoring among other things. You will
        also have the chance to dive deep into new blockchain protocols, run testnets,
        build secure and scalable infra and maintain it.
        ",
    "minimum_requirement": "
        #### Requirements

        * A BSc/BA degree in Computer Science or a relevant field
        ",
    "preferred_requirement": "
        ### What excites us about you?

        * You have experience as DevOps/SRE/Infrastructure engineer
        * You have experience managing server infrastructures with high availability requirements
        * You had designed secure networks, systems, and application architectures
        * You had set up and maintained software in both data centers and cloud environments
        * You have a deep understanding of sockets, full networking stack, and Linux security
        * You possess the knowledge of building automation and CI/CD processes and tools
        * You are experienced with Docker, Kubernetes, and other cloud deployment technologies
        * You have flexibility, teamwork, and you are comfortable with ambiguity, able to take charge and get things done despite the unknowns

        ### What will be great to have?

        * You have an understanding of the blockchain space and blockchain technology
        * You possess knowledge of cryptography and security best practices
        * You have contributions to open source communities

        If those describe you, this is the right opportunity for you!
        ",
    "responsibilities": "
        ### What will you do?

        * Build secure and reliable infrastructure to monitor, detect and mitigate performance and security issues
        * System administration activities for Linux servers, which includes routine, proactive daily management of the health, stability, and availability of system infrastructure
        * Create and maintain system procedural and technical documentation
        * Stay up to date and build on peer-to-peer networking security best practices
        * Create, maintain and communicate threat models + risk assessments for all systems we operate
        ",
    "compensation": "
        ### Why are we awesome you ask?

        We are a truly global team! We are digital nomads coming from more than 12
        different countries, working from wherever we want. We have a collective
        mission, to provide meaningful services and bring a unique value to users
        within the crypto space.

        We are looking for fun, curious, and committed individuals to swim with us!
        "
}
```

---

# How to implement your solution with us

- All the input job raw files is in the `/input` folder
- All of your output will be in the `/output` folder
- All you need to do is write your code in `handle.py` file, specifically is in `handle` function.
- To test your result, just the command:

```python
python3 handle.py
```
