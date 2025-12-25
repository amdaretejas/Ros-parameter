// Auto-generated. Do not edit!

// (in-package communication_model.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MotionCommand {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.source = null;
      this.linear_speed = null;
      this.angular_speed = null;
      this.acceleration = null;
      this.deceleration = null;
      this.enable_motion = null;
    }
    else {
      if (initObj.hasOwnProperty('source')) {
        this.source = initObj.source
      }
      else {
        this.source = '';
      }
      if (initObj.hasOwnProperty('linear_speed')) {
        this.linear_speed = initObj.linear_speed
      }
      else {
        this.linear_speed = 0.0;
      }
      if (initObj.hasOwnProperty('angular_speed')) {
        this.angular_speed = initObj.angular_speed
      }
      else {
        this.angular_speed = 0.0;
      }
      if (initObj.hasOwnProperty('acceleration')) {
        this.acceleration = initObj.acceleration
      }
      else {
        this.acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('deceleration')) {
        this.deceleration = initObj.deceleration
      }
      else {
        this.deceleration = 0.0;
      }
      if (initObj.hasOwnProperty('enable_motion')) {
        this.enable_motion = initObj.enable_motion
      }
      else {
        this.enable_motion = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotionCommand
    // Serialize message field [source]
    bufferOffset = _serializer.string(obj.source, buffer, bufferOffset);
    // Serialize message field [linear_speed]
    bufferOffset = _serializer.float32(obj.linear_speed, buffer, bufferOffset);
    // Serialize message field [angular_speed]
    bufferOffset = _serializer.float32(obj.angular_speed, buffer, bufferOffset);
    // Serialize message field [acceleration]
    bufferOffset = _serializer.float32(obj.acceleration, buffer, bufferOffset);
    // Serialize message field [deceleration]
    bufferOffset = _serializer.float32(obj.deceleration, buffer, bufferOffset);
    // Serialize message field [enable_motion]
    bufferOffset = _serializer.bool(obj.enable_motion, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotionCommand
    let len;
    let data = new MotionCommand(null);
    // Deserialize message field [source]
    data.source = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [linear_speed]
    data.linear_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angular_speed]
    data.angular_speed = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [acceleration]
    data.acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [deceleration]
    data.deceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [enable_motion]
    data.enable_motion = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.source);
    return length + 21;
  }

  static datatype() {
    // Returns string type for a message object
    return 'communication_model/MotionCommand';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9bfb8733eb8119d340ffa42ca50b6814';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string source        # who sent this message
    float32 linear_speed
    float32 angular_speed
    float32 acceleration
    float32 deceleration
    bool    enable_motion
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotionCommand(null);
    if (msg.source !== undefined) {
      resolved.source = msg.source;
    }
    else {
      resolved.source = ''
    }

    if (msg.linear_speed !== undefined) {
      resolved.linear_speed = msg.linear_speed;
    }
    else {
      resolved.linear_speed = 0.0
    }

    if (msg.angular_speed !== undefined) {
      resolved.angular_speed = msg.angular_speed;
    }
    else {
      resolved.angular_speed = 0.0
    }

    if (msg.acceleration !== undefined) {
      resolved.acceleration = msg.acceleration;
    }
    else {
      resolved.acceleration = 0.0
    }

    if (msg.deceleration !== undefined) {
      resolved.deceleration = msg.deceleration;
    }
    else {
      resolved.deceleration = 0.0
    }

    if (msg.enable_motion !== undefined) {
      resolved.enable_motion = msg.enable_motion;
    }
    else {
      resolved.enable_motion = false
    }

    return resolved;
    }
};

module.exports = MotionCommand;
