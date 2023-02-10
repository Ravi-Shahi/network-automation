#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def extract_utilization(string):
    parts = string.split(", ")
    txload = int(parts[1].split(" ")[-1].split("/")[0])
    rxload = int(parts[2].split(" ")[-1].split("/")[0])
    return txload, rxload

def calculate_utilization(txload, rxload):  
    tx_utilization =int(txload * 100 / 255)
    rx_utilization = int(rxload * 100 / 255)
    total_utilization = (tx_utilization + rx_utilization) / 2
    return total_utilization

def main():
    module = AnsibleModule(
        argument_spec=dict(
            string=dict(required=True, type='str')
        ),
        supports_check_mode=False
    )
    
    string = module.params['string']
    txload, rxload = extract_utilization(string)
    utilization = calculate_utilization(txload, rxload)
    
    result = dict(
        changed=False,
        utilization=utilization,
        txload=txload,
        rxload=rxload
    )
    module.exit_json(**result)

if __name__ == '__main__':
    main()
