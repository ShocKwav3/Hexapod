from machine import Pin

from constants import Constants


PCA9685Addresses = {
    Constants.RIGHT: 0x41,
    Constants.LEFT: 0x40,
}

i2cConfig = {
    Constants.SDA: Pin(3),
    Constants.SCL: Pin(4),
}

defaultStandAngles = {
    Constants.LEG_RIGHT_A: {
        Constants.COXA: [75],
        Constants.FEMUR: [0, 70],
        Constants.TIBIA: [0]
    },
    Constants.LEG_RIGHT_B: {
        Constants.COXA: [90],
        Constants.FEMUR: [0, 70],
        Constants.TIBIA: [0]
    },
    Constants.LEG_RIGHT_C: {
        Constants.COXA: [75],
        Constants.FEMUR: [0, 70],
        Constants.TIBIA: [0]
    },
    Constants.LEG_LEFT_D: {
        Constants.COXA: [75],
        Constants.FEMUR: [0, 70],
        Constants.TIBIA: [0]
    },
    Constants.LEG_LEFT_E: {
        Constants.COXA: [90],
        Constants.FEMUR: [0, 75],
        Constants.TIBIA: [0]
    },
    Constants.LEG_LEFT_F: {
        Constants.COXA: [75],
        Constants.FEMUR: [0, 70],
        Constants.TIBIA: [0]
    }
}

# Legs lettering done by going clock-wise from front
legs = {
    Constants.LEG_RIGHT_A: {
        Constants.LEG_NAME: Constants.LEG_RIGHT_A,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.RIGHT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 0,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.FEMUR,
            Constants.CHANNEL: 1,
            Constants.DEGREES_TO_ADJUST: 10,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 2,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        }
    },
    Constants.LEG_RIGHT_B: {
        Constants.LEG_NAME: Constants.LEG_RIGHT_B,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.RIGHT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 5,
            Constants.DEGREES_TO_ADJUST: 12,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.FEMUR,
            Constants.CHANNEL: 6,
            Constants.DEGREES_TO_ADJUST: 10,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 7,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
    },
    Constants.LEG_RIGHT_C: {
        Constants.LEG_NAME: Constants.LEG_RIGHT_C,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.RIGHT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 13,
            Constants.DEGREES_TO_ADJUST: 20,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: True
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.FEMUR,
            Constants.CHANNEL: 14,
            Constants.DEGREES_TO_ADJUST: 10,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 15,
            Constants.DEGREES_TO_ADJUST: -0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
    },
    Constants.LEG_LEFT_D: {
        Constants.LEG_NAME: Constants.LEG_LEFT_D,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.LEFT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 0,
            Constants.DEGREES_TO_ADJUST: -10,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: True
                },
                Constants.STANCE: {
                    Constants.INVERTED: True
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.FEMUR,
            Constants.CHANNEL: 1,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 2,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
    },
    Constants.LEG_LEFT_E: {
        Constants.LEG_NAME: Constants.LEG_LEFT_E,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.LEFT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 5,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: True
                },
                Constants.STANCE: {
                    Constants.INVERTED: True
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.FEMUR,
            Constants.CHANNEL: 6,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 7,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
    },
    Constants.LEG_LEFT_F: {
        Constants.LEG_NAME: Constants.LEG_LEFT_F,
        Constants.I2C_ADDRESS: PCA9685Addresses[Constants.LEFT],
        Constants.COXA: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 13,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: True
                },
                Constants.SWING: {
                    Constants.INVERTED: True
                },
                Constants.STANCE: {
                    Constants.INVERTED: True
                }
            }
        },
        Constants.FEMUR: {
            Constants.JOINT_NAME: Constants.COXA,
            Constants.CHANNEL: 14,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
        Constants.TIBIA: {
            Constants.JOINT_NAME: Constants.TIBIA,
            Constants.CHANNEL: 15,
            Constants.DEGREES_TO_ADJUST: 0,
            Constants.ACTIVITIES: {
                Constants.STAND: {
                    Constants.INVERTED: False
                },
                Constants.SWING: {
                    Constants.INVERTED: False
                },
                Constants.STANCE: {
                    Constants.INVERTED: False
                }
            }
        },
    },
}
