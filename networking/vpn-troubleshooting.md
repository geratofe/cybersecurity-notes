# VPN Troubleshooting (TryHackMe)

## Introduction

During a TryHackMe session, I encountered a problem where I could not connect to a target machine using `ssh`, `ping`, or `nmap`.

Even though the VPN appeared to be connected, the target machine was unreachable. After investigating the issue, I found that the VPN tunnel interfaces (`tun`) were in a broken state. This guide documents the troubleshooting process used to diagnose and fix the issue.

This documentation may help others experiencing similar VPN connectivity problems.

---

## Step 1 – Test Connectivity

The first step when a connection fails is to test basic network connectivity using `ping`.

```
ping <target-ip>
```

Example:

```
ping 10.49.167.137
```

`ping` sends small packets to a host to check whether it is reachable.

If the machine is reachable, you will see replies like:

```
64 bytes from 10.49.167.137
```

If the machine is unreachable, you may see:

```
100% packet loss
```

### Useful Ping Options

Limit the number of packets sent:

```
ping -c 4 <target-ip>
```

Example:

```
ping -c 4 10.49.167.137
```

This sends 4 packets and then stops.

If the ping test fails, the issue may be related to the VPN connection.

---

## Step 2 – Check and Clean Tunnel Interfaces

Next, check the VPN tunnel interfaces.

```
ip a | grep tun
```

Example problematic output:

```
tun0: state DOWN
tun1: state DOWN
```

Multiple tunnel interfaces or interfaces in a **DOWN** state may indicate a broken or incomplete VPN session.

### Removing Broken Tunnel Interfaces

To clean the VPN environment, remove the existing tunnel interfaces.

```
sudo ip link delete tun0
sudo ip link delete tun1
sudo ip link delete tun2
```

### Verify the Interfaces Were Removed

After deleting them, confirm that no tunnel interfaces remain.

```
ip a | grep tun
```

If the cleanup was successful, no `tun` interfaces should appear in the output.

Note: This solution worked in my case. Other setups may require different troubleshooting steps.

---

## Step 3 – Restart OpenVPN

After cleaning the old tunnel interfaces, restart the VPN connection.

```
sudo openvpn <vpn-config-file>.ovpn
```

Example:

```
sudo openvpn tryhackme.ovpn
```

Once the VPN reconnects successfully, a new tunnel interface should appear.

Verify it with:

```
ip a | grep tun
```

Example correct output:

```
tun0: <POINTOPOINT,NOARP,UP,LOWER_UP>
```

This indicates the VPN tunnel is active.

---

## Step 4 – Verify the Connection

After reconnecting to the VPN, test the connection again.

### Test with ping

```
ping <target-ip>
```

Example:

```
ping 10.49.167.137
```

### Test with nmap

```
nmap <target-ip>
```

### Test with ssh

```
ssh user@<target-ip>
```

Example:

```
ssh user@10.49.167.137
```

If these commands work, the VPN connection has been successfully restored.

---

## Possible Cause

One possible cause of this issue is improperly closing the OpenVPN process.

For example, using:

```
Ctrl + Z
```

This **suspends** the process instead of terminating it. When this happens, OpenVPN may leave behind active or partially configured `tun` interfaces.

These leftover interfaces can cause routing issues or prevent new VPN connections from working correctly.

Over time, multiple unused `tun` interfaces may accumulate and interfere with the network configuration.

---

## Personal Note

In my case, the issue was resolved by **manually deleting the existing `tun` interfaces and restarting OpenVPN**.

However, this solution worked for **my specific setup**, and the root cause may vary depending on the system configuration, VPN provider, or network environment.

If you experience similar issues, this method may help, but other troubleshooting approaches may also be required.
