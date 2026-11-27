// Recovery reference for the managed tools orchestrator, not a Node CLI.
// imagegen can return an inline data URL without output_hint or a saved PNG.
// Keep each shell argument below Linux's per-argument size limit. Base64 uses
// only safe literal characters. Never print image data in text logs.
async function preserveInlinePng(result, tag, tools) {
  const b64 = result.image_url.split(',')[1];
  const parts = [];
  for (let offset = 0; offset < b64.length; offset += 60000) {
    const file = '/workspace/scratch/' + tag + '-' + String(offset).padStart(9, '0') + '.part';
    const chunk = b64.slice(offset, offset + 60000);
    await tools.exec_command({
      cmd: `python -c 'import base64;open("${file}","wb").write(base64.b64decode("${chunk}"))'`,
      max_output_tokens: 100,
    });
    parts.push(file);
  }
  // Concatenate in the parts array's order into a .png under generated_images,
  // verify the PNG, copy the selected deliverable and preserve the source.
  // Use imagegen for any image alteration; copying raw returned bytes is only
  // artifact recovery and must not redraw or manipulate the generated image.
  return parts;
}
