#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_lag_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_lag_interfaces
short_description: Link Aggregation Juniper JUNOS resource module
description: This module manages properties of Link Aggregation Group on Juniper JUNOS
  devices.
version_added: 1.0.0
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the link aggregation group (LAG).
        type: str
        required: true
      mode:
        description:
        - LAG mode. A value of C(passive) will enable LACP in C(passive) mode that
          is it will respond to LACP packets and C(active) configures the link to
          initiate transmission of LACP packets.
        type: str
        choices:
        - active
        - passive
      link_protection:
        description:
        - This boolean option indicates if link protection should be enabled for the
          LAG interface. If value is C(True) link protection is enabled on LAG and
          if value is C(False) link protection is disabled.
        type: bool
      members:
        description:
        - List of member interfaces of the link aggregation group. The value can be
          single interface or list of interfaces.
        type: list
        elements: dict
        suboptions:
          member:
            description:
            - Name of the member interface.
            type: str
          link_type:
            description:
            - The value of this options configures the member link as either C(primary)
              or C(backup). Value C(primary) configures primary interface for link-protection
              mode and C(backup) configures backup interface for link-protection mode.
            type: str
            choices:
            - primary
            - backup
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show interfaces).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
requirements:
- ncclient (>=v0.6.4)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 18.4R1.
- This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#     description "lag interface 1";
# }

- name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
      - name: ae1
    state: deleted

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
            link_type: primary
          - member: ge-0/0/2
            link_type: backup
    state: merged

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad {
#            ae0;
#            primary;
#        }
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad {
#            ae0;
#            backup;
#        }
#    }
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae3 {
#     description "lag interface 3";
# }

- name: Overrides all device LAG configuration with provided configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/2
      - name: ae1
        members:
          - member: ge-0/0/1
        mode: passive
    state: overridden

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae1;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ae0 {
#     description "lag interface";
# }
# ae1 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }


# Using merged

# Before state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }

- name: Replace device LAG configuration with provided configuration
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae0
        members:
          - member: ge-0/0/1
        mode: active
    state: replaced

# After state:
# -------------
# user@junos01# show interfaces
# ge-0/0/1 {
#    description "Ansible configured interface 1";
#    ether-options {
#        802.3ad ae0;
#    }
# }
# ge-0/0/2 {
#    description "Ansible configured interface 2";
# }
# ae0 {
#    aggregated-ether-options {
#        lacp {
#            active;
#        }
#    }
# }
# ge-0/0/3 {
#    description "Ansible configured interface 3";
# }
# Using gathered
# Before state:
# ------------
#
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             ae2;
#             primary;
#         }
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad {
#             ae2;
#             backup;
#         }
#     }
# }
# ge-1/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.1/24;
#             address 10.200.16.20/24;
#         }
#         family inet6;
#     }
# }
# ge-2/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.2/24;
#             address 10.200.16.21/24;
#         }
#         family inet6;
#     }
# }
# ge-3/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.3/24;
#             address 10.200.16.22/24;
#         }
#         family inet6;
#     }
# }
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             active;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         link-protection;
#         lacp {
#             passive;
#         }
#     }
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }
- name: Gather junos lag interfaces as in given arguments
  junipernetworks.junos.junos_lag_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "members": [
#                 {
#                     "member": "ge-0/0/1"
#                 },
#                 {
#                     "member": "ge-0/0/2"
#                 }
#             ],
#             "mode": "active",
#             "name": "ae1"
#         },
#         {
#             "link_protection": true,
#             "members": [
#                 {
#                     "link_type": "primary",
#                     "member": "ge-0/0/3"
#                 },
#                 {
#                     "link_type": "backup",
#                     "member": "ge-0/0/4"
#                 }
#             ],
#             "mode": "passive",
#             "name": "ae2"
#         }
#     ]
# After state:
# ------------
#
# ansible@cm123456tr21# show interfaces
# ge-0/0/1 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/2 {
#     ether-options {
#         802.3ad ae1;
#     }
# }
# ge-0/0/3 {
#     ether-options {
#         802.3ad {
#             ae2;
#             primary;
#         }
#     }
# }
# ge-0/0/4 {
#     ether-options {
#         802.3ad {
#             ae2;
#             backup;
#         }
#     }
# }
# ge-1/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.1/24;
#             address 10.200.16.20/24;
#         }
#         family inet6;
#     }
# }
# ge-2/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.2/24;
#             address 10.200.16.21/24;
#         }
#         family inet6;
#     }
# }
# ge-3/0/0 {
#     unit 0 {
#         family inet {
#             address 192.168.100.3/24;
#             address 10.200.16.22/24;
#         }
#         family inet6;
#     }
# }
# ae1 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         lacp {
#             active;
#         }
#     }
# }
# ae2 {
#     description "Configured by Ansible";
#     aggregated-ether-options {
#         link-protection;
#         lacp {
#             passive;
#         }
#     }
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }
# Using parsed
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
# <interfaces>
#         <interface>
#             <name>ge-0/0/1</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/2</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae1</bundle>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/3</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                     <primary/>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-0/0/4</name>
#             <ether-options>
#                 <ieee-802.3ad>
#                     <bundle>ae2</bundle>
#                     <backup/>
#                 </ieee-802.3ad>
#             </ether-options>
#         </interface>
#         <interface>
#             <name>ge-1/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.1/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.20/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-2/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.2/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.21/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ge-3/0/0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>192.168.100.3/24</name>
#                         </address>
#                         <address>
#                             <name>10.200.16.22/24</name>
#                         </address>
#                     </inet>
#                     <inet6>
#                     </inet6>
#                 </family>
#             </unit>
#         </interface>
#         <interface>
#             <name>ae1</name>
#             <description>Configured by Ansible</description>
#             <aggregated-ether-options>
#                 <lacp>
#                     <active/>
#                 </lacp>
#             </aggregated-ether-options>
#         </interface>
#         <interface>
#             <name>ae2</name>
#             <description>Configured by Ansible</description>
#             <aggregated-ether-options>
#                 <link-protection>
#                 </link-protection>
#                 <lacp>
#                     <passive/>
#                 </lacp>
#             </aggregated-ether-options>
#         </interface>
#         <interface>
#             <name>em1</name>
#             <description>TEST</description>
#         </interface>
#         <interface>
#             <name>fxp0</name>
#             <description>ANSIBLE</description>
#             <speed>1g</speed>
#             <link-mode>automatic</link-mode>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <address>
#                             <name>10.8.38.38/24</name>
#                         </address>
#                     </inet>
#                 </family>
#             </unit>
#         </interface>
#     </interfaces>
#     </configuration>
# </rpc-reply>
# - name: Convert interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lag_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "members": [
#                 {
#                     "member": "ge-0/0/1"
#                 },
#                 {
#                     "member": "ge-0/0/2"
#                 }
#             ],
#             "mode": "active",
#             "name": "ae1"
#         },
#         {
#             "link_protection": true,
#             "members": [
#                 {
#                     "link_type": "primary",
#                     "member": "ge-0/0/3"
#                 },
#                 {
#                     "link_type": "backup",
#                     "member": "ge-0/0/4"
#                 }
#             ],
#             "mode": "passive",
#             "name": "ae2"
#         }
#     ]
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lag_interfaces:
    config:
      - name: ae1
        members:
          - member: ge-0/0/1
          - member: ge-0/0/2
        mode: active

      - name: ae2
        link_protection: true
        members:
          - member: ge-0/0/3
            link_type: primary
          - member: ge-0/0/4
            link_type: backup
        mode: passive
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:interfaces
#     xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#     <nc:interface>
#         <nc:name>ae1</nc:name>
#         <nc:aggregated-ether-options>
#             <nc:lacp>
#                 <nc:active/>
#             </nc:lacp>
#         </nc:aggregated-ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/1</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae1</nc:bundle>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae1</nc:bundle>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ae2</nc:name>
#         <nc:aggregated-ether-options>
#             <nc:lacp>
#                 <nc:passive/>
#             </nc:lacp>
#             <nc:link-protection/>
#         </nc:aggregated-ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/3</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae2</nc:bundle>
#                 <nc:primary/>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/4</nc:name>
#         <nc:ether-options>
#             <nc:ieee-802.3ad>
#                 <nc:bundle>ae2</nc:bundle>
#                 <nc:backup/>
#             </nc:ieee-802.3ad>
#         </nc:ether-options>
#     </nc:interface>
# </nc:interfaces>"
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
xml:
  description: The set of xml rpc payload pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:interfaces
    xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <nc:interface>
        <nc:name>ae1</nc:name>
        <nc:aggregated-ether-options>
            <nc:lacp>
                <nc:active/>
            </nc:lacp>
        </nc:aggregated-ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/1</nc:name>
        <nc:ether-options>
            <nc:ieee-802.3ad>
                <nc:bundle>ae1</nc:bundle>
            </nc:ieee-802.3ad>
        </nc:ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/2</nc:name>
        <nc:ether-options>
            <nc:ieee-802.3ad>
                <nc:bundle>ae1</nc:bundle>
            </nc:ieee-802.3ad>
        </nc:ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ae2</nc:name>
        <nc:aggregated-ether-options>
            <nc:lacp>
                <nc:passive/>
            </nc:lacp>
            <nc:link-protection/>
        </nc:aggregated-ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/3</nc:name>
        <nc:ether-options>
            <nc:ieee-802.3ad>
                <nc:bundle>ae2</nc:bundle>
                <nc:primary/>
            </nc:ieee-802.3ad>
        </nc:ether-options>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/4</nc:name>
        <nc:ether-options>
            <nc:ieee-802.3ad>
                <nc:bundle>ae2</nc:bundle>
                <nc:backup/>
            </nc:ieee-802.3ad>
        </nc:ether-options>
    </nc:interface>
</nc:interfaces>', 'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.lag_interfaces.lag_interfaces import (
    Lag_interfacesArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.lag_interfaces.lag_interfaces import (
    Lag_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]

    module = AnsibleModule(
        argument_spec=Lag_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
