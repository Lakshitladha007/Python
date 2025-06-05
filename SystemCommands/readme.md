## Subprocess Module

The subprocess module allows you to spawn new processes, run shell commands, and interact with their input/output.<br>
It's a safer, more powerful alternative to older modules like os.system().<br>

#### Common Use Cases:
1. Run shell/system commands (e.g., ls, cp, systemctl)
2. Capture output from commands
3. Automate system-level tasks like restarting services, installing packages, etc.

#### Important functions:
| Function               | Description                                               |

| `subprocess.run()`     | Runs a command, waits for it to finish                    |

| `subprocess.Popen()`   | Starts a process and gives more control over input/output |

| `subprocess.call()`    | Similar to `run()`, but returns only the return code      |

| `subprocess.check_output()`| Runs a command and returns the output                 |

| `subprocess.DEVNULL`   | Used to discard stdout or stderr                     |

## Shutil Module

The shutil module offers file operations for high-level tasks such as Copying, Moving, Deleting and Archiving (zip/tar)

#### Common Use Cases:
1. Rotate or backup log files
2. Create compressed backups (ZIP, TAR)
3. Automate file organization
4. Clean up old directories

#### Important functions:
| Function                            | Description                         |

| `shutil.copy(src, dst)`             | Copy a file                         |
| `shutil.copy2(src, dst)`            | Copy file with metadata             |
| `shutil.move(src, dst)`             | Move or rename a file               |
| `shutil.rmtree(path)`               | Delete a directory and its contents |
| `shutil.make_archive(base_name, format, root_dir)` | Create archive (zip, tar)      |
| `shutil.disk_usage(path)`                          | Check disk usage info          |
